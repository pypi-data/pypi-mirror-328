"""
Create agent page for AgentStudio
"""
import streamlit as st
from agentstudio.utils.agent_manager import AgentManager, create_agent
from agentstudio.utils.database import db
from agentstudio.utils.file_handler import handle_file_upload, cleanup_files
from agentstudio.utils.templates import get_agent_templates
from agentstudio.components.forms import render_config_form
import uuid
import asyncio
import logging
import os

logger = logging.getLogger(__name__)

def create_agent_page():
    st.title("Create New Agent")

    # Initialize all session state variables
    if 'create_step' not in st.session_state:
        st.session_state.create_step = 1
    if 'selected_template' not in st.session_state:
        st.session_state.selected_template = None
    if 'selected_agent' not in st.session_state:
        st.session_state.selected_agent = None
    if 'agent_config' not in st.session_state:
        st.session_state.agent_config = None
    if 'temp_dir' not in st.session_state:
        st.session_state.temp_dir = None

    # Load existing agents
    existing_agents = db.get_all_agents()

    # Display existing agents
    if existing_agents:
        st.subheader("Existing Agents")
        for agent in existing_agents:
            with st.expander(f"{agent['name']} ({agent['type']})"):
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.write(f"Description: {agent['description']}")
                    st.write(f"Created: {agent['created_at']}")
                with col2:
                    if st.button("Edit", key=f"edit_{agent['id']}"):
                        templates = get_agent_templates()
                        template = next((t for t in templates if t['id'] == agent['type']), None)
                        if template:
                            st.session_state.selected_template = template
                            st.session_state.selected_agent = agent
                            st.session_state.create_step = 2
                            st.rerun()
                        else:
                            st.error("Could not find matching template for agent type")
                with col3:
                    if st.button("Delete", key=f"delete_{agent['id']}"):
                        if db.delete_agent(agent['id']):
                            st.success(f"Deleted agent: {agent['name']}")
                            st.rerun()
        st.divider()

    # Step progress
    step = st.session_state.create_step
    st.progress(step / 3)

    if step == 1:
        st.subheader("Step 1: Choose Agent Template")
        templates = get_agent_templates()

        for template in templates:
            col1, col2 = st.columns([3,1])
            with col1:
                st.write(f"### {template['name']}")
                st.write(template['description'])
            with col2:
                if st.button("Select", key=f"template_{template['id']}"):
                    st.session_state.selected_template = template
                    st.session_state.create_step = 2
                    st.rerun()

    elif step == 2:
        if not st.session_state.selected_template:
            st.error("No template selected. Please go back and select a template first.")
            if st.button("← Back to Template Selection"):
                st.session_state.create_step = 1
                st.rerun()
            return

        st.subheader("Step 2: Configure Agent")
        template = st.session_state.selected_template
        existing_agent = st.session_state.selected_agent

        st.write(f"Configuring: {template['name']}")

        # Basic configuration
        agent_name = st.text_input("Agent Name", value=existing_agent['name'] if existing_agent else "")
        agent_description = st.text_area("Description", value=existing_agent['description'] if existing_agent else "")

        # Model configuration
        st.write("### Model Configuration")
        model_type = st.selectbox(
            "Model Type",
            options=["Default", "Custom"],
            help="Choose between predefined models or enter a custom model"
        )

        if model_type == "Default":
            model = st.selectbox(
                "Select Model",
                options=["openai/gpt-4o", "anthropic/claude-2", "google/gemini-pro"],
                help="Choose a predefined model"
            )
            model_config = {"type": "predefined", "selected": model}
        else:
            custom_model = st.text_input(
                "Custom Model",
                help="Enter a custom model identifier (e.g., 'openai/gpt-4-1106-preview')"
            )
            model_config = {"type": "custom", "value": custom_model}

        # Get available tools including custom tools
        available_tools = AgentManager._get_all_available_tools()
        logger.info(f"Available tools for agent configuration: {available_tools}")

        # Update template config schema with available tools
        if 'config_schema' in template and 'tools' in template['config_schema']:
            tools_field = template['config_schema']['tools']
            if 'options' in tools_field:
                tools_field['options'] = available_tools
                logger.info(f"Updated tool options in config schema: {tools_field['options']}")

        # Template-specific configuration
        config = render_config_form(template['config_schema'])

        # File upload section for RAG tool
        if 'tools' in config and 'RAGTool' in config['tools']:
            st.write("### Document Upload for RAG Tool")
            st.write("Upload documents to be processed by the RAG tool:")
            uploaded_files = st.file_uploader(
                "Choose files",
                accept_multiple_files=True,
                type=['txt', 'pdf', 'doc', 'docx']
            )

            if uploaded_files:
                temp_dir = handle_file_upload(uploaded_files, config)
                if temp_dir:
                    st.session_state.temp_dir = temp_dir

        if st.button("Next"):
            if agent_name and agent_description:
                agent_id = existing_agent['id'] if existing_agent else str(uuid.uuid4())
                st.session_state.agent_config = {
                    'id': agent_id,
                    'name': agent_name,
                    'description': agent_description,
                    'type': template['id'],
                    'config': config,
                    'model_config': model_config # Added model configuration
                }
                st.session_state.create_step = 3
                st.rerun()
            else:
                st.error("Please fill in all required fields")

    elif step == 3:
        if not st.session_state.agent_config:
            st.error("No agent configuration found. Please go back and configure the agent first.")
            if st.button("← Back to Configuration"):
                st.session_state.create_step = 2
                st.rerun()
            return

        st.subheader("Step 3: Review and Create")
        config = st.session_state.agent_config

        st.write("### Agent Configuration")
        st.write(f"Name: {config['name']}")
        st.write(f"Description: {config['description']}")
        st.write("### Technical Configuration")
        st.json(config['config'])
        st.write("### Model Configuration")
        st.json(config['model_config']) # Added to display model config

        if st.button("Create Agent"):
            try:
                with st.spinner("Creating agent..."):
                    # Create Hawkins agent
                    agent = asyncio.run(create_agent(config))

                    # Save to database
                    db.save_agent({
                        'id': config['id'],
                        'name': config['name'],
                        'description': config['description'],
                        'type': config['type'],
                        'config': config['config'],
                        'model_config': config['model_config'] # Added to save model config
                    })

                    # Clean up temp files after successful agent creation
                    if st.session_state.get('temp_dir'):
                        cleanup_files(st.session_state.temp_dir)
                        st.session_state.pop('temp_dir', None)

                    st.success("Agent created successfully!")
                    # Reset state
                    st.session_state.create_step = 1
                    st.session_state.pop('selected_template', None)
                    st.session_state.pop('agent_config', None)
                    st.session_state.pop('selected_agent', None)
                    st.rerun()
            except Exception as e:
                logger.exception("Error creating agent", exc_info=e)
                st.error(f"Error creating agent: {str(e)}")

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if step > 1:
            if st.button("← Back"):
                st.session_state.create_step = step - 1
                st.rerun()
    with col2:
        if st.button("Cancel"):
            # Clean up temp files on cancel
            if st.session_state.get('temp_dir'):
                cleanup_files(st.session_state.temp_dir)
                st.session_state.pop('temp_dir', None)

            st.session_state.create_step = 1
            st.session_state.pop('selected_template', None)
            st.session_state.pop('agent_config', None)
            st.session_state.pop('selected_agent', None)
            st.rerun()

if __name__ == "__main__":
    create_agent_page()