"""
Settings page for AgentStudio
"""
import streamlit as st
import os
from typing import Dict, Any
import json
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


def mask_value(value: str) -> str:
    """Mask sensitive values for display"""
    if not value:
        return ""
    return value[:4] + "*" * (len(value) - 4) if len(value) > 4 else "****"

def settings_page():
    st.title("Environment Settings")

    # Initialize session state for environment variables if not exists
    if 'environment_vars' not in st.session_state:
        st.session_state.environment_vars = {}
        # Load existing environment variables
        for key, value in os.environ.items():
            # Store all environment variables except system ones
            if not key.startswith(('PATH', 'PYTHONPATH', 'LANG', 'HOME', 'USER')):
                st.session_state.environment_vars[key] = value

    # Verify environment variables in system
    st.subheader("Environment Variable Verification")
    if st.button("Verify Environment Variables"):
        st.write("Currently accessible environment variables:")
        env_vars = {k: mask_value(v) for k, v in os.environ.items() 
                   if k in st.session_state.environment_vars}
        st.json(env_vars)

    # Display current environment variables
    st.subheader("Current Environment Variables")

    if st.session_state.environment_vars:
        for key, value in st.session_state.environment_vars.items():
            col1, col2, col3 = st.columns([3, 2, 1])
            with col1:
                st.text(key)
            with col2:
                st.text(mask_value(value))
            with col3:
                if st.button("Delete", key=f"delete_{key}"):
                    if key in os.environ:
                        del os.environ[key]
                    del st.session_state.environment_vars[key]
                    st.success(f"Deleted environment variable: {key}")
                    st.rerun()
    else:
        st.info("No environment variables set")

    # Add new environment variable
    st.subheader("Add New Environment Variable")

    with st.form("add_env_var"):
        new_key = st.text_input("Variable Name", 
                               help="Enter the name of your environment variable")
        new_value = st.text_input("Value", type="password")

        # Validation
        submitted = st.form_submit_button("Add Variable")
        if submitted and new_key and new_value:
            try:
                # Validate key format
                if not new_key.replace('_', '').isalnum():
                    st.error("Variable name should only contain letters, numbers, and underscores")
                    return

                # Add to both os.environ and session state
                os.environ[new_key] = new_value
                st.session_state.environment_vars[new_key] = new_value

                logger.info(f"Added new environment variable: {new_key}")
                st.success(f"Added environment variable: {new_key}")
                st.rerun()
            except Exception as e:
                logger.error(f"Error adding environment variable: {str(e)}")
                st.error(f"Failed to add environment variable: {str(e)}")
        elif submitted:
            st.error("Please fill in both fields")

    # Documentation
    with st.expander("📚 Environment Variables Guide"):
        st.write("""
        ### Adding Environment Variables

        You can add any environment variable that your application needs:

        - **API Keys**: Add your API keys for various services
        - **Configuration Variables**: Add custom configuration values
        - **Application Settings**: Add application-specific settings

        ### Naming Conventions

        - Use UPPERCASE letters
        - Use underscores (_) to separate words
        - Use descriptive names that indicate the purpose

        Examples:
        - `DATABASE_URL`
        - `API_KEY`
        - `CUSTOM_SETTING`

        ### Security Notes

        - Environment variables are stored in memory only
        - Values are masked when displayed
        - Use secure, unique values for sensitive data
        - Regularly rotate sensitive values like API keys
        """)

if __name__ == "__main__":
    settings_page()