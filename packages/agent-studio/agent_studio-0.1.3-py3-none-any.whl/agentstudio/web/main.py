"""
Streamlit interface for AgentStudio
"""
import os
import sys
import streamlit as st
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Adjust path to include the repository root
try:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
    logger.debug(f"Added to path: {os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))}")
except Exception as e:
    logger.error(f"Error setting up path: {str(e)}")
    raise

try:
    from agentstudio.components.sidebar import render_sidebar
    from agentstudio.utils.database import db
except Exception as e:
    logger.error(f"Error importing modules: {str(e)}")
    raise

try:
    st.set_page_config(
        page_title="Hawkins Agent Studio",
        page_icon="🤖",
        layout="wide"
    )
except Exception as e:
    logger.error(f"Error configuring Streamlit page: {str(e)}")
    raise

def initialize_session_state():
    """Initialize all required session state variables"""
    try:
        if 'current_agent' not in st.session_state:
            st.session_state.current_agent = None
        if 'create_step' not in st.session_state:
            st.session_state.create_step = 1
        if 'environment_vars' not in st.session_state:
            st.session_state.environment_vars = {}
            # Load existing environment variables
            for key, value in os.environ.items():
                if key.startswith(('OPENAI_', 'ANTHROPIC_', 'TWILIO_', 'STRIPE_', 'HAWKINS_')):
                    st.session_state.environment_vars[key] = value
        logger.debug("Session state initialized successfully")
    except Exception as e:
        logger.error(f"Error initializing session state: {str(e)}")
        raise

def main():
    try:
        # Initialize session state
        initialize_session_state()

        # Render sidebar
        render_sidebar()

        # Main content
        st.title("🤖 Hawkins Agent Studio")
        st.subheader("No-Code AI Agent Creation Platform")

        # Important notice for users
        st.warning("""
        Important Notice: This AI agent platform is currently intended for local and development environments only. 
        It is not yet production-ready and if you are first time user we recommend you check tutorial page before 
        using this tool to build agents and workflows.
        """)

        # Get agents from database
        try:
            agents = db.get_all_agents()
            logger.debug(f"Retrieved {len(agents)} agents from database")
        except Exception as e:
            logger.error(f"Error getting agents from database: {str(e)}")
            agents = []

        # Dashboard overview
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Agents", len(agents))
        with col2:
            st.metric("Active Agents", len([a for a in agents if a.get('status') == 'active']))
        with col3:
            st.metric("Deployed Agents", len([a for a in agents if a.get('deployed')]))
        with col4:
            if st.button("⚙️ Settings", key="main_settings_btn"):
                st.switch_page("pages/settings.py")

        # Agent listing
        st.subheader("Your Agents")
        if not agents:
            st.info("No agents created yet. Click 'Create New Agent' to get started!")
        else:
            for agent in agents:
                with st.expander(f"Agent: {agent['name']}"):
                    col1, col2, col3 = st.columns([2,1,1])
                    with col1:
                        st.write(f"Type: {agent['type']}")
                        st.write(f"Description: {agent['description']}")
                    with col2:
                        st.write(f"Status: {agent.get('status', 'inactive')}")
                    with col3:
                        st.button("Edit", key=f"edit_{agent['id']}")
                        st.button("Delete", key=f"delete_{agent['id']}")

    except Exception as e:
        logger.error(f"Error in main function: {str(e)}")
        st.error(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    try:
        logger.info("Starting AgentStudio web interface...")
        main()
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        raise