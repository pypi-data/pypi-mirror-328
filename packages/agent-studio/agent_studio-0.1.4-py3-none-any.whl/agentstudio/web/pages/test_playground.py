"""
Test playground page for AgentStudio
"""
import streamlit as st
import asyncio
from agentstudio.utils.agent_manager import test_agent
from agentstudio.utils.database import db


def test_playground_page():
    st.title("Agent Testing Playground")

    # Load agents from database
    available_agents = db.get_all_agents()

    # Agent selection
    if not available_agents:
        st.warning("No agents available for testing. Create an agent first!")
        return

    selected_agent = st.selectbox(
        "Select Agent to Test",
        options=available_agents,
        format_func=lambda x: f"{x['name']} ({x['type']})"
    )

    # Test configuration
    st.subheader("Test Configuration")

    # Input section
    st.write("### Input")
    input_type = selected_agent.get('input_type', 'text')

    user_input = None
    if input_type == 'text':
        user_input = st.text_area("Enter your input")
    elif input_type == 'file':
        user_input = st.file_uploader("Upload input file")

    # Test controls
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Run Test"):
            if user_input:
                with st.spinner("Running test..."):
                    try:
                        # Run async test in sync context
                        result = asyncio.run(test_agent(selected_agent, user_input))
                        st.session_state.test_result = result
                    except Exception as e:
                        st.error(f"Test failed: {str(e)}")
    with col2:
        if st.button("Clear Results"):
            st.session_state.pop('test_result', None)

    # Results section
    if 'test_result' in st.session_state:
        st.write("### Results")
        result = st.session_state.test_result

        # Display main output
        st.write("#### Response")
        st.write(result['output'])

        # Display tool calls if present
        if 'tool_calls' in result:
            st.write("#### Tool Calls")
            for call in result['tool_calls']:
                st.write(f"Tool: {call['name']}")
                st.write(f"Parameters: {call['parameters']}")

        # Display tool results if present
        if 'tool_results' in result:
            st.write("#### Tool Results")
            for tool_result in result['tool_results']:
                if tool_result.get('success'):
                    st.success(f"Result: {tool_result['result']}")
                else:
                    st.error(f"Error: {tool_result['error']}")

        # Performance metrics
        st.write("### Performance Metrics")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Response Time", f"{result.get('response_time', 0):.2f}s")
        with col2:
            st.metric("Memory Usage", f"{result.get('memory_usage', 0)}MB")

if __name__ == "__main__":
    test_playground_page()