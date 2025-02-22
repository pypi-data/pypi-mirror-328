"""
Create workflow page for AgentStudio
"""
import streamlit as st
from agentstudio.utils.database import db
import logging
from agentstudio.utils.flow_manager import FlowManager, FlowStep, StepDescription
from agentstudio.utils.agent_manager import test_agent
import asyncio
import json
import uuid
import logging
from datetime import datetime
import requests
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_workflow_page():
    st.title("Create Agent Workflow")

    # Initialize session state variables
    if 'workflow_steps' not in st.session_state:
        st.session_state.workflow_steps = []  # Serializable step definitions
    if 'workflow_manager' not in st.session_state:
        st.session_state.workflow_manager = FlowManager()  # Should have an attribute (e.g., steps) to store flow steps
    if 'workflow_name' not in st.session_state:
        st.session_state.workflow_name = ""
    if 'workflow_description' not in st.session_state:
        st.session_state.workflow_description = ""
    if 'current_workflow_id' not in st.session_state:
        st.session_state.current_workflow_id = None
    if 'test_results' not in st.session_state:
        st.session_state.test_results = None

    try:
        # Load existing workflows and available agents from the database
        existing_workflows = db.get_all_workflows()
        available_agents = db.get_all_agents()

        if not available_agents:
            st.warning("No agents available for workflows. Create an agent first!")
            return

        # --- Existing Workflows Section ---
        if existing_workflows:
            st.subheader("Existing Workflows")
            for workflow in existing_workflows:
                with st.expander(f"{workflow['name']} ({len(workflow.get('steps', []))} steps)"):
                    col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
                    with col1:
                        st.write(f"Description: {workflow.get('description', '')}")
                        st.write(f"Created: {workflow.get('created_at', '')}")
                        st.write(f"Number of steps: {len(workflow.get('steps', []))}")
                    with col2:
                        if st.button("Load", key=f"load_{workflow['id']}"):
                            try:
                                logger.info(f"Loading workflow: {workflow['name']}")
                                st.session_state.workflow_manager = FlowManager()
                                st.session_state.workflow_name = workflow['name']
                                st.session_state.workflow_description = workflow.get('description', '')
                                st.session_state.current_workflow_id = workflow['id']

                                # Process and load steps from stored workflow definitions.
                                processed_steps = []
                                for step in workflow.get('steps', []):
                                    processed_step = {
                                        'name': step.get('name', 'unnamed_step'),
                                        'description': step.get('description', ''),
                                        'agent': step.get('agent', {}),
                                        'requires': step.get('requires', []),
                                        'requirements': step.get('requirements', []),
                                        'format_instructions': step.get('format_instructions', ''),
                                        'memory_config': step.get('memory_config', {
                                            'memory_types': ['Short-term'],
                                            'retention_days': 30
                                        })
                                    }
                                    processed_steps.append(processed_step)

                                    # Create a step description for display
                                    step_desc = StepDescription(
                                        objective=processed_step['description'],
                                        requirements=processed_step['requirements'],
                                        format_instructions=processed_step['format_instructions']
                                    )

                                    async def process_step(input_data: Dict[str, Any], context: Dict[str, Any], step_config=processed_step):
                                        try:
                                            dependencies = step_config.get('requires', [])
                                            if dependencies:
                                                logger.info(f"Step '{step_config['name']}' waiting for dependencies: {dependencies}")
                                                # Wait until all dependency outputs are in context
                                                while not all(dep in context for dep in dependencies):
                                                    logger.debug(f"Current context keys: {list(context.keys())}")
                                                    await asyncio.sleep(0.1)
                                                # Use first dependency's output as input (customize if needed)
                                                dep = dependencies[0]
                                                dep_output = context[dep].get('output', '')
                                                input_data = {'input': dep_output}
                                                logger.info(f"Step '{step_config['name']}' received dependency output from '{dep}'")
                                            else:
                                                logger.info(f"Step '{step_config['name']}' using direct input")

                                            prompt = f"""
                                            Purpose: {step_config.get('description', '')}
                                            Input: {json.dumps(input_data, indent=2)}
                                            Requirements: {json.dumps(step_config.get('requirements', []), indent=2)}
                                            Format Instructions: {step_config.get('format_instructions', '')}
                                            """
                                            logger.info(f"Step '{step_config['name']}' executing with prompt: {prompt}")
                                            result = await test_agent(step_config['agent'], prompt)
                                            if not isinstance(result, dict):
                                                result = {'output': str(result)}
                                            if 'output' not in result:
                                                result['output'] = result.get('result', '')
                                            result['timestamp'] = datetime.now().isoformat()
                                            result['metadata'] = {
                                                'step_name': step_config['name'],
                                                'agent_type': step_config['agent'].get('type', 'unknown'),
                                                'description': step_config.get('description', ''),
                                                'memory_config': step_config.get('memory_config', {})
                                            }
                                            return result
                                        except Exception as e:
                                            logger.error(f"Error in step '{step_config['name']}': {str(e)}")
                                            raise

                                    # Create a flow step and add it to the manager
                                    flow_step = FlowStep(
                                        name=processed_step['name'],
                                        agent=processed_step['agent'],
                                        process=process_step,
                                        description=step_desc,
                                        requires=processed_step['requires']
                                    )
                                    st.session_state.workflow_manager.add_step(flow_step)
                                st.session_state.workflow_steps = processed_steps
                                st.success(f"Loaded workflow: {workflow['name']}")
                                st.rerun()
                            except Exception as e:
                                logger.error(f"Error loading workflow: {str(e)}")
                                st.error(f"Error loading workflow: {str(e)}")
                    with col3:
                        if st.button("Run", key=f"run_{workflow['id']}"):
                            st.session_state.current_workflow_id = workflow['id']
                            with st.form(key="run_workflow_form"):
                                test_input = st.text_area("Test Input")
                                submitted = st.form_submit_button("Execute Workflow")
                                if submitted and test_input:
                                    try:
                                        # Reset manager for execution
                                        st.session_state.workflow_manager = FlowManager()
                                        # Recreate flow steps from stored definitions
                                        for step in workflow.get('steps', []):
                                            step_desc = StepDescription(
                                                objective=step.get('description', ''),
                                                requirements=step.get('requirements', []),
                                                format_instructions=step.get('format_instructions', '')
                                            )
                                            async def process_step(input_data: Dict[str, Any], context: Dict[str, Any], step_config=step):
                                                try:
                                                    dependencies = step_config.get('requires', [])
                                                    if dependencies:
                                                        logger.info(f"Step '{step_config['name']}' waiting for dependencies: {dependencies}")
                                                        while not all(dep in context for dep in dependencies):
                                                            await asyncio.sleep(0.1)
                                                        dep = dependencies[0]
                                                        dep_output = context[dep].get('output', '')
                                                        input_data = {'input': dep_output}
                                                        logger.info(f"Step '{step_config['name']}' received dependency output from '{dep}'")
                                                    else:
                                                        logger.info(f"Step '{step_config['name']}' using direct input")

                                                    prompt = f"""
                                                    Purpose: {step_config.get('description', '')}
                                                    Input: {json.dumps(input_data, indent=2)}
                                                    Requirements: {json.dumps(step_config.get('requirements', []), indent=2)}
                                                    Format Instructions: {step_config.get('format_instructions', '')}
                                                    """
                                                    result = await test_agent(step_config['agent'], prompt)
                                                    if not isinstance(result, dict):
                                                        result = {'output': str(result)}
                                                    if 'output' not in result:
                                                        result['output'] = result.get('result', '')
                                                    result['timestamp'] = datetime.now().isoformat()
                                                    result['metadata'] = {
                                                        'step_name': step_config['name'],
                                                        'agent_type': step_config['agent'].get('type', 'unknown'),
                                                        'description': step_config.get('description', ''),
                                                        'memory_config': step_config.get('memory_config', {})
                                                    }
                                                    return result
                                                except Exception as e:
                                                    logger.error(f"Error in step '{step_config['name']}': {str(e)}")
                                                    raise

                                            flow_step = FlowStep(
                                                name=step['name'],
                                                agent=step['agent'],
                                                process=process_step,
                                                description=step_desc,
                                                requires=step.get('requires', [])
                                            )
                                            st.session_state.workflow_manager.add_step(flow_step)

                                        # Execute workflow by iterating over the FlowManager's steps
                                        async def execute_workflow():
                                            context = {}
                                            # Assuming FlowManager stores steps in a list called `steps`
                                            for flow_step in st.session_state.workflow_manager.steps:
                                                logger.info(f"Executing step: {flow_step.name}")
                                                result = await flow_step.process({'input': test_input}, context)
                                                context[flow_step.name] = result
                                            return context

                                        results = asyncio.run(execute_workflow())
                                        st.session_state.test_results = results
                                        st.success("Workflow execution completed")
                                    except Exception as e:
                                        logger.error(f"Workflow execution failed: {str(e)}")
                                        st.error(f"Workflow execution failed: {str(e)}")
                    with col4:
                        if st.button("Delete", key=f"delete_{workflow['id']}"):
                            if db.delete_workflow(workflow['id']):
                                st.success(f"Deleted workflow: {workflow['name']}")
                                if st.session_state.current_workflow_id == workflow['id']:
                                    st.session_state.workflow_steps = []
                                    st.session_state.workflow_manager = FlowManager()
                                    st.session_state.workflow_name = ""
                                    st.session_state.workflow_description = ""
                                    st.session_state.current_workflow_id = None
                                st.rerun()

            st.divider()

        # --- Workflow Metadata Input ---
        col1, col2 = st.columns(2)
        with col1:
            new_workflow_name = st.text_input("Workflow Name", value=st.session_state.workflow_name,
                                                help="Give your workflow a descriptive name")
            if new_workflow_name != st.session_state.workflow_name:
                st.session_state.workflow_name = new_workflow_name
        with col2:
            new_workflow_description = st.text_area("Workflow Description", value=st.session_state.workflow_description,
                                                     help="Describe what this workflow does")
            if new_workflow_description != st.session_state.workflow_description:
                st.session_state.workflow_description = new_workflow_description

        # --- Step Configuration ---
        st.subheader("Add Workflow Step")
        with st.form(key="add_step_form"):
            step_name = st.text_input("Step Name")
            step_objective = st.text_area("Step Objective", help="What is the main goal of this step?")
            step_requirements = st.text_area("Step Requirements", help="List the key requirements (one per line)")
            format_instructions = st.text_area("Format Instructions", help="Optional: Specify the output format")
            selected_agent = st.selectbox("Select Agent", options=available_agents,
                                          format_func=lambda x: f"{x['name']} ({x['type']})")
            # Memory configuration
            memory_types = st.multiselect("Memory Types", options=["Short-term", "Long-term", "Semantic"],
                                          default=["Short-term"])
            retention_days = st.slider("Memory Retention (days)", min_value=1, max_value=90, value=30)
            # Dependency handling: allow user to pick an existing step as dependency.
            prev_step_names = [step['name'] for step in st.session_state.workflow_steps]
            dependency = st.selectbox("Depends on Step", options=["None"] + prev_step_names,
                                      help="Select which step must complete before this one")
            dependencies = [] if dependency == "None" else [dependency]
            submitted = st.form_submit_button("Add Step")

        if submitted and step_name and selected_agent and step_objective and step_requirements:
            try:
                requirement_list = [r.strip() for r in step_requirements.split('\n') if r.strip()]
                # Optionally, automatically add dependency to previous step if none selected
                if st.session_state.workflow_steps and dependency == "None":
                    last_step = st.session_state.workflow_steps[-1]
                    dependencies = [last_step['name']]
                    logger.info(f"Automatically setting dependency for step '{step_name}' to previous step '{last_step['name']}'")
                serializable_step = {
                    'name': step_name,
                    'description': step_objective,
                    'agent': selected_agent,
                    'requires': dependencies,
                    'memory_config': {
                        'memory_types': memory_types,
                        'retention_days': retention_days
                    },
                    'requirements': requirement_list,
                    'format_instructions': format_instructions
                }
                st.session_state.workflow_steps.append(serializable_step)

                # Create a step description for display purposes.
                step_desc = StepDescription(
                    objective=step_objective,
                    requirements=requirement_list,
                    format_instructions=format_instructions if format_instructions else None
                )

                async def process_step(input_data: Dict[str, Any], context: Dict[str, Any], step_config=serializable_step):
                    try:
                        dependencies = step_config.get('requires', [])
                        if dependencies:
                            logger.info(f"Step '{step_config['name']}' waiting for dependency: {dependencies}")
                            while not all(dep in context for dep in dependencies):
                                await asyncio.sleep(0.1)
                            dep = dependencies[0]
                            dep_output = context[dep].get('output', '')
                            input_data = {'input': dep_output}
                        else:
                            logger.info(f"Step '{step_config['name']}' using direct input")
                        prompt = f"""
                        Purpose: {step_config.get('description', '')}
                        Input: {json.dumps(input_data, indent=2)}
                        Requirements: {json.dumps(step_config.get('requirements', []), indent=2)}
                        Format Instructions: {step_config.get('format_instructions', '')}
                        """
                        result = await test_agent(step_config['agent'], prompt)
                        if not isinstance(result, dict):
                            result = {'output': str(result)}
                        if 'output' not in result:
                            result['output'] = result.get('result', '')
                        result['timestamp'] = datetime.now().isoformat()
                        result['metadata'] = {
                            'step_name': step_config['name'],
                            'agent_type': step_config['agent'].get('type', 'unknown'),
                            'description': step_config.get('description', ''),
                            'memory_config': step_config.get('memory_config', {})
                        }
                        return result
                    except Exception as e:
                        logger.error(f"Error in step '{step_config['name']}': {str(e)}")
                        raise

                flow_step = FlowStep(
                    name=step_name,
                    agent=selected_agent,
                    process=process_step,
                    description=step_desc,
                    requires=dependencies
                )
                st.session_state.workflow_manager.add_step(flow_step)

                if st.session_state.workflow_name:
                    workflow_id = st.session_state.current_workflow_id or str(uuid.uuid4())
                    db.save_workflow({
                        'id': workflow_id,
                        'name': st.session_state.workflow_name,
                        'description': st.session_state.workflow_description,
                        'steps': st.session_state.workflow_steps,
                        'created_at': datetime.now().isoformat(),
                        'deployed': False
                    })
                    st.session_state.current_workflow_id = workflow_id
                    st.success("Workflow saved!")
            except Exception as e:
                st.error(f"Failed to add step: {str(e)}")
                logger.error(f"Error adding step: {str(e)}")
        elif submitted:
            st.error("Please fill in all required fields")

        # --- Display Current Workflow and Testing ---
        if st.session_state.workflow_steps:
            st.subheader("Current Workflow")
            workflow_tab, results_tab = st.tabs(["Workflow Steps", "Test Results"])
            with workflow_tab:
                for i, step in enumerate(st.session_state.workflow_steps):
                    st.write(f"### Step {i+1}: {step['name']}")
                    col1, col2 = st.columns([2, 1])
                    with col1:
                        st.write("**Description:**", step['description'])
                        st.write("**Agent:**", step['agent']['name'])
                        st.write("**Dependencies:**", step.get('requires', []))
                    with col2:
                        st.write("**Config Details:**")
                        st.json({
                            'agent_type': step['agent'].get('type', 'unknown'),
                            'memory_config': step.get('memory_config', {}),
                            'requirements': step.get('requirements', [])
                        })
                    st.divider()
            with results_tab:
                if st.session_state.test_results:
                    st.write("### Workflow Test Results")
                    st.json(st.session_state.test_results)
            with st.form(key="test_workflow_form"):
                test_input = st.text_area("Test Input", help="Enter input for your workflow")
                if st.form_submit_button("Run Workflow"):
                    if test_input:
                        try:
                            async def execute_workflow():
                                context = {}
                                for flow_step in st.session_state.workflow_manager.steps:
                                    logger.info(f"Executing step: {flow_step.name}")
                                    result = await flow_step.process({'input': test_input}, context)
                                    context[flow_step.name] = result
                                return context
                            results = asyncio.run(execute_workflow())
                            st.session_state.test_results = results
                            st.success("Workflow execution completed")
                        except Exception as e:
                            logger.error(f"Workflow execution failed: {str(e)}")
                            st.error(f"Workflow execution failed: {str(e)}")
                    else:
                        st.error("Please provide test input")

        # --- Save and Deploy Workflow ---
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Save Workflow"):
                if st.session_state.workflow_name:
                    try:
                        workflow_id = st.session_state.current_workflow_id or str(uuid.uuid4())
                        workflow_data = {
                            'id': workflow_id,
                            'name': st.session_state.workflow_name,
                            'description': st.session_state.workflow_description,
                            'steps': st.session_state.workflow_steps,
                            'created_at': datetime.now().isoformat(),
                            'deployed': False
                        }
                        db.save_workflow(workflow_data)
                        st.session_state.current_workflow_id = workflow_id
                        st.success("Workflow saved successfully!")
                    except Exception as e:
                        st.error(f"Failed to save workflow: {str(e)}")
                        logger.error(f"Error saving workflow: {str(e)}")
                else:
                    st.error("Please provide a workflow name")
        with col2:
            if st.button("Deploy Workflow"):
                if not st.session_state.workflow_name:
                    st.error("Please save the workflow before deploying")
                else:
                    try:
                        workflow_id = st.session_state.current_workflow_id
                        if not workflow_id:
                            st.error("Please save the workflow before deploying")
                            return
                        workflow_data = {
                            'id': workflow_id,
                            'name': st.session_state.workflow_name,
                            'description': st.session_state.workflow_description,
                            'steps': st.session_state.workflow_steps,
                            'deployed': True,
                            'created_at': datetime.now().isoformat(),
                            'deployed_at': datetime.now().isoformat()
                        }
                        response = requests.post(
                            'http://localhost:8000/api/deploy',
                            json=workflow_data
                        )
                        if response.status_code == 200:
                            st.success(f"Workflow {st.session_state.workflow_name} deployed successfully!")
                            with st.expander("📋 API Usage Examples", expanded=True):
                                example_input = {"input": f"Test input for workflow '{st.session_state.workflow_name}'"}
                                st.code(f"""
curl -X POST http://localhost:8000/api/process/{workflow_id} \\
  -H "Content-Type: application/json" \\
  -d '{json.dumps(example_input)}'
""", language="bash")
                        else:
                            st.error(f"Failed to deploy workflow: {response.json().get('detail', 'Unknown error')}")
                    except Exception as e:
                        st.error(f"Failed to deploy workflow: {str(e)}")
                        logger.error(f"Error deploying workflow: {str(e)}")
        # --- Workflow Management Buttons ---
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Reset Workflow"):
                st.session_state.workflow_manager = FlowManager()
                st.success("Workflow reset")
                st.rerun()
        with col2:
            if st.button("Clear All Steps"):
                st.session_state.workflow_steps = []
                st.session_state.workflow_manager = FlowManager()
                st.session_state.workflow_name = ""
                st.session_state.workflow_description = ""
                st.session_state.current_workflow_id = None
                st.success("Workflow cleared")
                st.rerun()
    except Exception as e:
        logger.error(f"Error in create_workflow_page: {str(e)}")
        st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    create_workflow_page()
