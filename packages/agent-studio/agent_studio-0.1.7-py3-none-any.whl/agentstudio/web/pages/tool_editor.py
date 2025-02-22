"""
Tool editor page for AgentStudio
"""
import streamlit as st
import os
import json
from typing import Dict, Any
from hawkins_agent.tools import BaseTool
from hawkins_agent.types import ToolResponse, AgentResponse

def tool_editor_page():
    st.title("Custom Tool Editor")

    # Initialize session state
    if 'custom_tools' not in st.session_state:
        st.session_state.custom_tools = {}
        # Load existing tools
        custom_tools_dir = 'custom_tools'
        if os.path.exists(custom_tools_dir):
            for filename in os.listdir(custom_tools_dir):
                if filename.endswith('_meta.json'):
                    try:
                        with open(os.path.join(custom_tools_dir, filename), 'r') as f:
                            tool_meta = json.load(f)
                            tool_name = os.path.splitext(filename)[0].replace('_meta', '')
                            st.session_state.custom_tools[tool_name] = tool_meta
                    except Exception as e:
                        st.error(f"Error loading tool metadata: {str(e)}")

    # Tool creation form
    st.subheader("Create New Tool")

    with st.form("new_tool_form"):
        tool_name = st.text_input("Tool Name")
        tool_description = st.text_area("Tool Description")

        code_template = '''from hawkins_agent.tools import BaseTool
from hawkins_agent.types import ToolResponse, AgentResponse
from typing import Dict, Any

class CustomTool(BaseTool):
    """A custom tool implementation"""

    def __init__(self, name: str):
        """Initialize your tool"""
        super().__init__(name=name)

    @property
    def description(self) -> str:
        """Tool description used by the agent"""
        return "[Your tool description here]"

    def validate_params(self, params: Dict[str, Any]) -> bool:
        """Validate input parameters"""
        if 'query' not in params:
            return False
        if not isinstance(params['query'], str):
            return False
        return True

    async def execute(self, **kwargs) -> ToolResponse:
        """Execute the tool's functionality"""
        try:
            query = kwargs.get('query', '')
            # Your tool logic here
            result = "Tool execution result"

            # Wrap the response in AgentResponse format
            agent_response = AgentResponse(
                message=result,
                tool_calls=[],
                metadata={}
            )

            return ToolResponse(
                success=True,
                result=agent_response,
                error=None
            )
        except Exception as e:
            return ToolResponse(
                success=False,
                result=None,
                error=str(e)
            )
'''

        tool_code = st.text_area("Tool Implementation", value=code_template, height=400)

        # Form submission
        submitted = st.form_submit_button("Create Tool")
        if submitted:
            try:
                if not tool_name or not tool_description or not tool_code:
                    st.error("Please fill in all fields")
                    return

                # Create custom_tools directory if it doesn't exist
                os.makedirs('custom_tools', exist_ok=True)

                # Save tool implementation
                tool_file = os.path.join('custom_tools', f"{tool_name.lower()}.py")
                with open(tool_file, 'w') as f:
                    f.write(tool_code)

                # Save tool metadata
                tool_meta = {
                    'name': tool_name,
                    'description': tool_description,
                    'type': 'custom'
                }

                meta_file = os.path.join('custom_tools', f"{tool_name.lower()}_meta.json")
                with open(meta_file, 'w') as f:
                    json.dump(tool_meta, f, indent=2)

                st.session_state.custom_tools[tool_name.lower()] = tool_meta
                st.success(f"Tool '{tool_name}' created successfully!")
                st.rerun()

            except Exception as e:
                st.error(f"Error creating tool: {str(e)}")

    # Display existing tools
    st.subheader("Existing Tools")

    if not st.session_state.custom_tools:
        st.info("No custom tools created yet")
    else:
        for tool_name, tool_meta in st.session_state.custom_tools.items():
            with st.expander(f"{tool_meta['name']} - {tool_meta['description']}"):
                try:
                    tool_file = os.path.join('custom_tools', f"{tool_name}.py")
                    if os.path.exists(tool_file):
                        with open(tool_file, 'r') as f:
                            st.code(f.read(), language='python')
                except Exception as e:
                    st.error(f"Error loading tool code: {str(e)}")

if __name__ == "__main__":
    tool_editor_page()