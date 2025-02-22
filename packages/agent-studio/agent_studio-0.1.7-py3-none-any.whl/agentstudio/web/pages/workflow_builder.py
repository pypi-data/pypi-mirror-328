"""
Visual workflow builder interface
"""
import streamlit as st
import asyncio
from uuid import uuid4
import logging
from datetime import datetime
import json
from typing import Dict, Any
from streamlit_flow import (
    streamlit_flow, 
    StreamlitFlowNode, 
    StreamlitFlowEdge,
    StreamlitFlowState
)
from streamlit_flow.layouts import TreeLayout
from agentstudio.utils.flow_manager import FlowManager, FlowStep, StepDescription
from agentstudio.utils.database import db
from agentstudio.utils.agent_manager import test_agent

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_session_state():
    """Initialize session state with default workflow data"""
    if 'workflow_state' not in st.session_state:
        initial_node = StreamlitFlowNode(id='start',
                                         pos=(100, 100),
                                         data={
                                             'content':
                                             '# Start\nInitial workflow step',
                                             'type': 'start',
                                             'agent': None,
                                             'description': '',
                                             'requirements': [],
                                             'connections': {}
                                         },
                                         node_type='input',
                                         source_position='right',
                                         style={
                                             'backgroundColor': '#4CAF50',
                                             'color': 'white',
                                             'border': '2px solid white',
                                             'borderRadius': '8px',
                                             'padding': '10px',
                                             'minWidth': '150px',
                                             'minHeight': '60px'
                                         })
        st.session_state.workflow_state = StreamlitFlowState([initial_node],
                                                             [])

    if 'workflow_name' not in st.session_state:
        st.session_state.workflow_name = ""
    if 'workflow_description' not in st.session_state:
        st.session_state.workflow_description = ""
    if 'workflow_manager' not in st.session_state:
        st.session_state.workflow_manager = FlowManager()
    if 'current_workflow_id' not in st.session_state:
        st.session_state.current_workflow_id = None
    if 'test_input' not in st.session_state:
        st.session_state.test_input = ""
    if 'workflow_results' not in st.session_state:
        st.session_state.workflow_results = {}

    logger.info("Session state initialized with keys: " +
                ", ".join(st.session_state.keys()))
    logger.info(
        f"workflow_results: {json.dumps(st.session_state.workflow_results, indent=2)}"
    )


def get_node_name(node: StreamlitFlowNode) -> str:
    """Extract node name (friendly name) from content."""
    return node.data['content'].split('\n')[0].replace('# ', '')


def get_connected_nodes(node_id: str, edges: list) -> dict:
    """Return dictionary of input and output node IDs for a given node."""
    input_nodes = [e.source for e in edges if e.target == node_id]
    output_nodes = [e.target for e in edges if e.source == node_id]
    return {'inputs': input_nodes, 'outputs': output_nodes}


# --- Modified process step creation ---
async def create_process_step(node_data, node_name):
    """
    Creates a process step function for a workflow node.
    This function maps any dependency (stored as a node ID in the node's
    connections) to its friendly name (via get_node_name) and looks that up
    in the execution context (or in st.session_state.workflow_results as fallback).
    """

    async def process_step(input_data: Dict[str, Any],
                           context: Dict[str, Any]) -> Dict[str, Any]:
        try:
            connections = node_data.get('connections', {})
            input_nodes = connections.get('inputs', [])
            if input_nodes:
                # Get dependency node id from connections.
                dep_node_id = input_nodes[0]
                # Map dependency node ID to its friendly name.
                dep_node = next((n
                                 for n in st.session_state.workflow_state.nodes
                                 if n.id == dep_node_id), None)
                if dep_node:
                    dep_friendly = get_node_name(dep_node)
                    if dep_friendly in context:
                        prev_output = context[dep_friendly].get('output', '')
                        input_data = {'input': prev_output}
                        logger.info(
                            f"[{node_name}] Using output from dependency '{dep_friendly}' found in context."
                        )
                    elif dep_friendly in st.session_state.workflow_results:
                        prev_output = st.session_state.workflow_results[
                            dep_friendly].get('output', '')
                        input_data = {'input': prev_output}
                        logger.info(
                            f"[{node_name}] Using output from dependency '{dep_friendly}' from workflow_results."
                        )
                    else:
                        logger.warning(
                            f"[{node_name}] Dependency '{dep_friendly}' not found in context or workflow_results."
                        )
                else:
                    logger.warning(
                        f"[{node_name}] Could not find dependency node for id '{dep_node_id}'."
                    )
            else:
                logger.info(
                    f"[{node_name}] No dependency found. Using provided input."
                )

            prompt = f"""
Purpose: {node_data['description']}
Input: {json.dumps(input_data, indent=2)}
Context: {json.dumps(context, indent=2)}
Requirements: {json.dumps(node_data['requirements'], indent=2)}
            """
            result = await test_agent(node_data['agent'], prompt)
            result['timestamp'] = datetime.now().isoformat()
            result['metadata'] = {
                'step_name': node_name,
                'agent_type': node_data['agent'].get('type', 'unknown'),
                'description': node_data.get('description', ''),
                'connections': {
                    'inputs': input_nodes,
                    'outputs': connections.get('outputs', [])
                }
            }
            return result
        except Exception as e:
            logger.error(f"Error in step {node_name}: {str(e)}")
            raise

    return process_step


async def setup_workflow_steps(nodes, node_steps):
    """
    Sets up all workflow steps asynchronously.
    In the first pass, we create steps (using the node's friendly name as the step key).
    In the second pass, we update each step's dependencies.
    """
    for node in nodes:
        if node.data.get('agent'):  # Only create steps for nodes with agents.
            node_name = get_node_name(node)
            step_desc = StepDescription(objective=node.data['description'],
                                        requirements=node.data['requirements'],
                                        format_instructions='')
            process_fn = await create_process_step(node.data, node_name)
            flow_step = FlowStep(
                name=node_name,  # Use friendly name as key.
                agent=node.data['agent'],
                process=process_fn,
                description=step_desc,
                requires=[]  # Dependencies updated below.
            )
            st.session_state.workflow_manager.add_step(flow_step)
            node_steps[node.id] = flow_step
            logger.info(f"Added step: {node_name}")

    # Second pass: update dependencies using friendly names.
    for node in nodes:
        if node.data.get('agent'):
            connections = node.data.get('connections', {})
            input_nodes = connections.get('inputs', [])
            if input_nodes:
                dep_node_id = input_nodes[0]
                dep_node = next((n for n in nodes if n.id == dep_node_id),
                                None)
                if dep_node:
                    dep_friendly = get_node_name(dep_node)
                    current_step = node_steps.get(node.id)
                    if current_step:
                        current_step.requires.append(dep_friendly)
                        logger.info(
                            f"Step '{get_node_name(node)}' now requires '{dep_friendly}'"
                        )


async def execute_workflow(input_data: dict):
    """Execute workflow with input data and store results in session state."""
    try:
        logger.info(
            f"Starting workflow execution with input: {json.dumps(input_data, indent=2)}"
        )
        results = await st.session_state.workflow_manager.execute(input_data)
        if results:
            logger.info("Workflow execution completed successfully")
            st.session_state.workflow_results = results
            return True
        logger.warning("Workflow execution returned no results")
        return False
    except Exception as e:
        logger.error(f"Error in workflow execution: {str(e)}", exc_info=True)
        raise


def display_workflow_results():
    """Display workflow results with friendly names."""
    try:
        results = st.session_state.get('workflow_results')
        if not results:
            logger.info("No workflow results found in session state")
            return

        st.write("### Workflow Results")
        # Map friendly names (used as keys) for display.
        node_map = {
            get_node_name(n): get_node_name(n)
            for n in st.session_state.workflow_state.nodes
        }
        for step_name, result in results.items():
            friendly = node_map.get(step_name, step_name)
            with st.expander(f"Step: {friendly}", expanded=True):
                try:
                    if isinstance(result, dict):
                        if 'output' in result:
                            st.markdown("#### Output")
                            st.write(result['output'])
                        if 'tool_calls' in result and result['tool_calls']:
                            st.markdown("#### Tools Used")
                            for tool in result['tool_calls']:
                                st.markdown(
                                    f"- **{tool.get('name', 'Unknown Tool')}**"
                                )
                                if 'parameters' in tool:
                                    st.code(json.dumps(tool['parameters'],
                                                       indent=2),
                                            language='json')
                        if 'metadata' in result:
                            st.markdown("#### Metadata")
                            st.write(result['metadata'])
                    else:
                        st.write(str(result))
                except Exception as e:
                    st.error(f"Error displaying step {friendly}: {str(e)}")
                    logger.error(f"Error in step result display: {str(e)}")
    except Exception as e:
        logger.error(f"Error displaying results: {str(e)}", exc_info=True)
        st.error(f"Failed to display results: {str(e)}")


def workflow_builder_page():
    st.title("Visual Workflow Builder")
    init_session_state()

    left_col, right_col = st.columns([3, 1])
    with right_col:
        st.subheader("Workflow Details")
        workflow_name = st.text_input(
            "Workflow Name",
            value=st.session_state.workflow_name,
            help="Give your workflow a descriptive name")
        if workflow_name != st.session_state.workflow_name:
            st.session_state.workflow_name = workflow_name

        workflow_description = st.text_area(
            "Description",
            value=st.session_state.workflow_description,
            help="Describe what this workflow does")
        if workflow_description != st.session_state.workflow_description:
            st.session_state.workflow_description = workflow_description

        st.divider()

        # Node Configuration
        if st.session_state.workflow_state.selected_id:
            st.subheader("Node Configuration")
            selected_id = st.session_state.workflow_state.selected_id
            selected_node = next(
                (n for n in st.session_state.workflow_state.nodes
                 if n.id == selected_id), None)
            if selected_node:
                with st.form(key=f"node_config_{selected_id}"):
                    node_name = st.text_input(
                        "Step Name", value=get_node_name(selected_node))
                    node_description = st.text_area(
                        "Description",
                        value=selected_node.data.get('description', ''))
                    st.write("### Input Configuration")
                    available_nodes = [
                        n for n in st.session_state.workflow_state.nodes
                        if n.id not in [selected_id, 'start']
                    ]
                    if available_nodes:
                        connections = get_connected_nodes(
                            selected_id, st.session_state.workflow_state.edges)
                        current_input = connections['inputs'][
                            0] if connections['inputs'] else None
                        available_node_ids = [n.id for n in available_nodes]
                        current_index = available_node_ids.index(
                            current_input
                        ) + 1 if current_input in available_node_ids else 0
                        input_node = st.selectbox(
                            "Get input from step",
                            options=["None"] +
                            [get_node_name(n) for n in available_nodes],
                            index=current_index,
                            key=f"input_{selected_id}")
                        if input_node != "None":
                            source_node = next(
                                (n for n in available_nodes
                                 if get_node_name(n) == input_node), None)
                            if source_node:
                                edges = [
                                    e for e in
                                    st.session_state.workflow_state.edges
                                    if e.target != selected_id
                                ]
                                new_edge = StreamlitFlowEdge(
                                    id=f"e_{source_node.id}-{selected_id}",
                                    source=source_node.id,
                                    target=selected_id)
                                edges.append(new_edge)
                                st.session_state.workflow_state.edges = edges
                                st.info(f"✓ Input from: {input_node}")
                        else:
                            st.session_state.workflow_state.edges = [
                                e
                                for e in st.session_state.workflow_state.edges
                                if e.target != selected_id
                            ]
                            st.info("✓ No input connection")
                    else:
                        st.info("✓ First step - no input needed")

                    available_agents = db.get_all_agents()
                    if available_agents:
                        selected_agent = st.selectbox(
                            "Select Agent",
                            options=available_agents,
                            format_func=lambda x: f"{x['name']} ({x['type']})")
                    else:
                        st.warning(
                            "No agents available. Create an agent first!")
                        selected_agent = None

                    requirements = st.text_area(
                        "Requirements",
                        value='\n'.join(
                            selected_node.data.get('requirements', [])),
                        help="List requirements (one per line)")

                    if st.form_submit_button("Update Node"):
                        try:
                            requirements_list = [
                                r.strip() for r in requirements.split('\n')
                                if r.strip()
                            ]
                            new_content = f"# {node_name}\n{node_description}"
                            connections = get_connected_nodes(
                                selected_id,
                                st.session_state.workflow_state.edges)
                            selected_node.data.update({
                                'content': new_content,
                                'description': node_description,
                                'agent': selected_agent,
                                'requirements': requirements_list,
                                'connections': {
                                    'inputs': connections['inputs'],
                                    'outputs': connections['outputs']
                                }
                            })
                            st.success(f"Updated node: {node_name}")
                        except Exception as e:
                            st.error(f"Failed to update node: {str(e)}")
        if st.button("Save Workflow"):
            if st.session_state.workflow_name:
                try:
                    steps = []
                    for node in st.session_state.workflow_state.nodes:
                        if node.data.get('agent'):
                            step = {
                                'name': get_node_name(node),
                                'description': node.data['description'],
                                'agent': node.data['agent'],
                                'requires': [],  # Dependencies set via edges.
                                'requirements': node.data['requirements'],
                                'format_instructions': ''
                            }
                            steps.append(step)
                    workflow_id = st.session_state.current_workflow_id or str(
                        uuid4())
                    workflow_data = {
                        'id': workflow_id,
                        'name': st.session_state.workflow_name,
                        'description': st.session_state.workflow_description,
                        'steps': steps,
                        'created_at': datetime.now().isoformat(),
                        'deployed': False
                    }
                    db.save_workflow(workflow_data)
                    st.session_state.current_workflow_id = workflow_id
                    st.success("Workflow saved successfully!")
                except Exception as e:
                    st.error(f"Failed to save workflow: {str(e)}")
            else:
                st.error("Please provide a workflow name")

        st.divider()
        st.subheader("Run Workflow")
        test_input = st.text_area("Input",
                                  value=st.session_state.test_input,
                                  key="workflow_test_input",
                                  help="Enter input for your workflow")
        if test_input != st.session_state.test_input:
            st.session_state.test_input = test_input
        if st.button("Run Workflow"):
            if not st.session_state.workflow_name:
                st.error("Please save the workflow first")
            elif not test_input:
                st.error("Please provide input")
            else:
                try:
                    st.session_state.workflow_manager = FlowManager(
                    )  # Reset manager
                    node_steps = {}
                    asyncio.run(
                        setup_workflow_steps(
                            st.session_state.workflow_state.nodes, node_steps))
                    with st.spinner("Running workflow..."):
                        success = asyncio.run(
                            execute_workflow({'input': test_input}))
                        if success:
                            st.success("Workflow execution completed!")
                        else:
                            st.warning(
                                "Workflow execution completed but returned no results"
                            )
                except Exception as e:
                    logger.error(f"Error during execution: {str(e)}",
                                 exc_info=True)
                    st.error(f"Workflow execution failed: {str(e)}")
        if st.session_state.workflow_results:
            display_workflow_results()
        st.divider()
    with left_col:
        updated_state = streamlit_flow('workflow_builder',
                                       st.session_state.workflow_state,
                                       fit_view=True,
                                       show_controls=True,
                                       show_minimap=True,
                                       allow_new_edges=True,
                                       animate_new_edges=True,
                                       enable_pane_menu=True,
                                       enable_node_menu=True,
                                       enable_edge_menu=True,
                                       get_node_on_click=True,
                                       get_edge_on_click=True,
                                       layout=TreeLayout("right"),
                                       height=700)
        if updated_state:
            st.session_state.workflow_state = updated_state
            if updated_state.selected_id:
                logger.info(f"Selected element: {updated_state.selected_id}")


if __name__ == "__main__":
    workflow_builder_page()