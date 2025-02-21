"""
Sidebar component for the Streamlit interface
"""
import streamlit as st
from typing import Dict, Any
import os

def render_sidebar() -> None:
    """Render the application sidebar"""
    with st.sidebar:
        st.title("🛠️ Controls")

        # Navigation
        st.subheader("Navigation")
        if st.button("🏠 Dashboard", key="nav_dashboard"):
            st.switch_page("main.py")
        if st.button("➕ Create Agent", key="nav_create_agent"):
            st.switch_page("pages/create_agent.py")
        if st.button("📊 Workflows", key="nav_workflows"):
            st.switch_page("pages/workflow_builder.py")
        if st.button("⚙️ Settings", key="nav_settings"):
            st.switch_page("pages/settings.py")

        # Environment Variables
        st.divider()
        st.subheader("Environment Variables")
        if 'environment_vars' in st.session_state:
            for key, value in st.session_state.environment_vars.items():
                # Show key and masked value
                st.text_input(
                    key,
                    value,
                    type="password",
                    disabled=True,
                    key=f"env_{key}"
                )

        # Add New Variable
        with st.expander("➕ Add New Variable"):
            new_key = st.text_input("Variable Name", key="new_var_name")
            new_value = st.text_input("Value", type="password", key="new_var_value")
            if st.button("Add", key="add_env_var"):
                if new_key and new_value:
                    if 'environment_vars' not in st.session_state:
                        st.session_state.environment_vars = {}
                    st.session_state.environment_vars[new_key] = new_value
                    os.environ[new_key] = new_value
                    st.success(f"Added {new_key}")
                    st.rerun()

        # Links
        st.divider()
        st.markdown("""
        * [📚 Documentation](https://github.com/username/agent-studio#readme)
        * [💡 Report Issue](https://github.com/username/agent-studio/issues)
        * [🤝 Contributing](https://github.com/username/agent-studio/blob/main/CONTRIBUTING.md)
        """)

        # Version info
        st.divider()
        from agentstudio import __version__
        st.caption(f"Version {__version__}")