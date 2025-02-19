import streamlit as st

def tutorial_page():
    st.title("Hawkins Agent Studio Tutorial")

    # Development Environment Notice
    st.warning("""
    ⚠️ **Important Notice**: This AI agent platform is currently intended for local and development environments only. 
    It is not yet production-ready and should not be used in production environments.
    """)

    # Getting Started
    st.header("Getting Started")

    # Environment Variables Setup Section
    with st.expander("1. Setting Up Environment Variables", expanded=True):
        st.write("""
        Before using the platform, you need to set up your environment variables:

        ### Method 1: Using Settings Page
        1. Navigate to the Settings page
        2. Add the required API keys and environment variables
        3. Save your settings

        ### Method 2: Windows Command Line Setup
        For Windows users, set environment variables via Command Prompt (Run as Administrator):
        """)

        st.code("""
        # OpenAI API Key
        setx OPENAI_API_KEY "your-api-key"

        # Anthropic API Key
        setx ANTHROPIC_API_KEY "your-api-key"

        # Other Service API Keys
        setx SERVICE_API_KEY "your-api-key"
        """, language="bash")

        st.info("""
        **Important:**
        - Replace "your-api-key" with actual API keys
        - Restart Command Prompt after setting variables
        - Restart the application to apply changes
        """)

    # Custom Tool Implementation Section
    with st.expander("2. Implementing Custom Tools", expanded=True):
        st.write("""
        ### Step 1: Tool Implementation Process
        1. Open the Tool Editor page
        2. Click "Add New Tool"
        3. Follow the template below for implementation

        ### Step 2: Required Code Structure
        Your tool must follow this structure:
        """)

        st.code("""
        from hawkins_agent.tools import BaseTool
        from hawkins_agent.types import ToolResponse
        from typing import Dict, Any

        class CustomTool(BaseTool):
            \"\"\"A custom tool implementation\"\"\"

            def __init__(self, name: str):
                \"\"\"Initialize your tool\"\"\"
                super().__init__(name=name)

            @property
            def description(self) -> str:
                \"\"\"Tool description used by the agent\"\"\"
                return "[Your tool description here]"

            def validate_params(self, params: Dict[str, Any]) -> bool:
                \"\"\"Validate input parameters\"\"\"
                if 'query' not in params:
                    return False
                if not isinstance(params['query'], str):
                    return False
                return True

            async def execute(self, **kwargs) -> ToolResponse:
                \"\"\"Execute the tool's functionality\"\"\"
                try:
                    query = kwargs.get('query', '')
                    # Your tool logic here
                    result = "Tool execution result"
                    return ToolResponse(
                        success=True,
                        result=result,
                        error=None
                    )
                except Exception as e:
                    return ToolResponse(
                        success=False,
                        result=None,
                        error=str(e)
                    )
        """, language="python")

        st.write("""
        ### Critical Requirements:
        1. **Class Inheritance**
           - Must inherit from `hawkins_agent.tools.BaseTool`
           - Import required types from hawkins_agent.types

        2. **Required Methods**
           - `__init__`: Initialize your tool with a name
           - `description`: Property that returns tool description
           - `validate_params`: Validate input parameters
           - `execute`: Main async implementation

        3. **Tool Response**
           - Always return a `ToolResponse` object
           - Include success status, result, and error information
           - Handle exceptions properly

        4. **Parameter Validation**
           - Implement thorough parameter validation
           - Return boolean indicating validity
           - Check required parameters and types

        5. **Error Handling**
           - Use try-except blocks in execute method
           - Return detailed error messages in ToolResponse
           - Never expose sensitive information in errors
        """)

    # Creating and Managing Agents Section
    with st.expander("3. Creating and Managing Agents", expanded=True):
        st.write("""
        ### Creating a New Agent
        1. Navigate to the 'Create Agent' page
        2. Configure agent settings:
           - Agent Name: Choose a descriptive name
           - Description: Define the agent's purpose
           - Memory Config: Set up memory settings
           - Model: Select LLM model
           - Tools: Choose required tools
           - Personality: Define agent's behavior and tone
        3. Test your agent in the playground

        ### Managing Existing Agents
        In the Create Agent page:
        - Edit agent configurations
        - Modify memory settings
        - Update tools and personality
        - Test changes in real-time
        """)

    # Building Workflows Section
    with st.expander("4. Building Workflows", expanded=True):
        st.write("""
        ### Method 1: Standard Workflow Creation (Create Workflow Page)
        1. Initial Setup:
           - Navigate to Create Workflow page
           - Add workflow Name and Description
           - These details help identify your workflow later

        2. Adding Workflow Steps:
           - **Step Name**: Give your step a clear, descriptive name
           - **Step Objective**: Define the specific goal for this step - be clear about what you need
           - **Step Requirements**: List key requirements in a clear and concise manner
           - **Format Instructions**: Optional - specify how the output should be formatted
           - **Select Agent**: Choose an appropriate agent for this step
           - **Memory Types**: Select appropriate options or leave default
           - **Memory Retention**: Leave default unless specific duration needed
           - **Depends on Step**: Specify if this step needs output from previous steps

        3. Testing and Deployment:
           - Click "Save Workflow" to store your configuration
           - To test: Enter input in "Test Input" field and click "Run Workflow"
           - View results in the "Test Results" tab
           - Click "Deploy Workflow" when ready to deploy

        ### Method 2: Visual Workflow Builder
        1. Initial Setup:
           - Navigate to Visual Workflow Builder
           - Add workflow name and description
           - You'll see a blank canvas for your workflow

        2. Creating and Configuring Nodes:
           - Right-click on canvas to create new node
           - Give the node a name
           - Click on created node to configure:
              * Step Name: Clear, descriptive name
              * Step Objective: Define the specific goal
              * Step Requirements: List key requirements
              * Format Instructions: Optional output format
              * Select Agent: Choose appropriate agent
              * Depends on Step: Configure input dependencies

        3. Connecting and Managing Nodes:
           - Connect nodes that share dependencies
           - Arrows show data flow between steps
           - Repeat node creation and configuration for each step
           - Ensure proper connection for steps needing previous outputs

        4. Workflow Management:
           - Save your workflow when complete
           - Test workflow with sample inputs
           - You can load this workflow in Create Workflow page
           - Deploy workflow from either Create Workflow or Visual Builder

        ### Important Notes:
        - Always save your workflow before testing or deployment
        - Test thoroughly with various inputs before deployment
        - You can load saved workflows using the "Load" button
        - Test or deploy workflows after loading them
        - All workflows can be managed from the Create Workflow page
        """)

    # Deployment Section
    with st.expander("5. Deploying Workflows", expanded=True):
        st.write("""
        ### Deployment Options
        1. API Deployment:
           - Deploy as REST API
           - Get endpoint details
           - View usage examples

        2. Integration:
           - API documentation
           - Authentication setup
           - Rate limiting options

        ### Example API Usage:
        """)

        st.code("""
        # Using curl
        curl -X POST http://your-api-endpoint/api/process \\
             -H "Content-Type: application/json" \\
             -d '{"input": "your input data"}'

        # Using Python requests
        import requests
        response = requests.post(
            'http://your-api-endpoint/api/process',
            json={'input': 'your input data'}
        )
        """, language="python")

    # Best Practices Section
    st.header("Best Practices")
    best_practices = {
        "Tool Development": [
            "Keep tools focused on single responsibility",
            "Implement comprehensive error handling",
            "Document input/output requirements",
            "Use type hints for better code clarity"
        ],
        "Agent Design": [
            "Define clear agent purposes",
            "Configure appropriate memory settings",
            "Test thoroughly in playground",
            "Monitor performance metrics"
        ],
        "Workflow Creation": [
            "Break complex tasks into steps",
            "Define clear dependencies",
            "Handle errors gracefully",
            "Document each step clearly"
        ],
        "Security": [
            "Never hardcode credentials",
            "Use environment variables for sensitive data",
            "Implement proper input validation",
            "Handle errors without exposing sensitive information"
        ]
    }

    for category, practices in best_practices.items():
        with st.expander(category):
            for practice in practices:
                st.write(f"• {practice}")

    # Feedback Section
    st.divider()
    st.write("### Was this tutorial helpful?")
    col1, col2, _ = st.columns([1, 1, 2])
    with col1:
        st.button("👍 Yes")
    with col2:
        st.button("👎 No")

if __name__ == "__main__":
    tutorial_page()