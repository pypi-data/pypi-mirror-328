"""
Agent management utilities for AgentStudio
"""
import uuid
from typing import Dict, Any, List, Optional
import time
import asyncio
import os
import json
import importlib.util
import sys
import logging
from hawkins_agent import AgentBuilder, Message
from hawkins_agent.mock import Document
from hawkins_agent.llm import LiteLLMProvider
from hawkins_agent.tools import WebSearchTool, RAGTool, SummarizationTool, WeatherTool
from hawkins_rag import HawkinsRAG
from ..tools.rag_tool import AgentStudioRAGTool

# Set up logging
logger = logging.getLogger(__name__)

async def _execute_tool(tool: Any, parameters: Dict[str, Any]) -> Dict[str, Any]:
    """Execute a tool and handle its response properly"""
    try:
        logger.debug(f"Starting tool execution: {tool.name} with parameters: {parameters}")

        # Handle async execution with proper wrapping
        try:
            if hasattr(tool, '_wrap_sync_query'):
                # Use tool's built-in sync wrapper if available
                logger.debug("Using tool's sync wrapper")
                result = await tool._wrap_sync_query(parameters.get('query', ''))
            elif hasattr(tool.execute, '__await__'):
                # Direct async execution
                logger.debug("Using direct async execution")
                result = await tool.execute(**parameters)
            else:
                # Wrap sync execution in async context
                logger.debug("Wrapping sync execution")
                loop = asyncio.get_event_loop()
                result = await loop.run_in_executor(None, lambda: tool.execute(**parameters))

            logger.debug(f"Raw tool execution result: {result}")

            # Standardize the result format
            if hasattr(result, 'success') and hasattr(result, 'result'):
                # Handle ToolResponse objects
                return {
                    'success': result.success,
                    'result': str(result.result) if result.result else None,
                    'error': result.error if hasattr(result, 'error') else None
                }
            elif isinstance(result, dict):
                # Handle dictionary responses
                return {
                    'success': True,
                    'result': str(result.get('response', result)),
                    'error': None
                }
            else:
                # Handle any other response type
                return {
                    'success': True,
                    'result': str(result),
                    'error': None
                }

        except Exception as exec_error:
            logger.error(f"Tool execution error: {str(exec_error)}", exc_info=True)
            return {
                'success': False,
                'result': None,
                'error': str(exec_error)
            }

    except Exception as e:
        logger.error(f"Tool execution wrapper error: {str(e)}", exc_info=True)
        return {
            'success': False,
            'result': None,
            'error': f"Tool execution wrapper error: {str(e)}"
        }

class AgentManager:
    @staticmethod
    def _convert_message_to_dict(message: Any) -> Dict[str, Any]:
        """Convert a Message object or dict to a JSON-serializable dictionary"""
        if isinstance(message, dict):
            return {
                'role': str(message.get('role', '')),
                'content': str(message.get('content', ''))
            }
        if hasattr(message, 'role') and hasattr(message, 'content'):
            return {
                'role': str(getattr(message, 'role', '')),
                'content': str(getattr(message, 'content', ''))
            }
        return {'role': 'user', 'content': str(message)}

    @staticmethod
    def _load_custom_tools() -> List[Dict[str, Any]]:
        """Load custom tools from the custom_tools directory"""
        custom_tools = []
        custom_tools_dir = 'custom_tools'

        if not os.path.exists(custom_tools_dir):
            return custom_tools

        for filename in os.listdir(custom_tools_dir):
            if filename.endswith('_meta.json'):
                try:
                    with open(os.path.join(custom_tools_dir, filename), 'r') as f:
                        tool_meta = json.load(f)

                    # Get the corresponding .py file
                    py_file = filename.replace('_meta.json', '.py')
                    if os.path.exists(os.path.join(custom_tools_dir, py_file)):
                        custom_tools.append(tool_meta)
                except Exception as e:
                    logger.error(f"Error loading custom tool {filename}: {str(e)}")

        return custom_tools

    @staticmethod
    def _get_tools(tool_names: list, rag_instance: Optional[HawkinsRAG] = None) -> list:
        """Get tool instances based on tool names"""
        # Map tools to their implementations
        tool_map = {
            'WebSearchTool': WebSearchTool,
            'RAGTool': AgentStudioRAGTool,  # Use our new RAG tool implementation
            'SummarizationTool': SummarizationTool,
            'WeatherTool': WeatherTool
        }

        # Initialize requested tools
        tools = []
        for name in tool_names:
            try:
                if name in tool_map:
                    tool = tool_map[name]()
                    if tool:
                        tools.append(tool)
                        logger.info(f"Successfully initialized tool: {name}")
                    else:
                        logger.warning(f"Failed to initialize tool: {name}")
            except Exception as e:
                logger.error(f"Error initializing tool {name}: {str(e)}")

        return tools

    @staticmethod
    async def create_agent(config: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new agent with the given configuration using Hawkins Agent SDK"""
        try:
            agent_id = str(uuid.uuid4())

            # Initialize RAG system
            rag = HawkinsRAG()

            # Load documents for RAG if provided
            rag_documents_dir = config['config'].get('rag_documents_dir')
            if rag_documents_dir:
                rag_documents_dir = resolve_rag_dir(rag_documents_dir)
                if rag_documents_dir:
                    try:
                        logger.info(f"Loading RAG documents from: {rag_documents_dir}")
                        for filename in os.listdir(rag_documents_dir):
                            file_path = os.path.join(rag_documents_dir, filename)
                            if os.path.isfile(file_path):
                                try:
                                    # Determine source type based on file extension
                                    ext = os.path.splitext(filename)[1].lower().lstrip('.')
                                    source_type_map = {
                                        'pdf': 'pdf',
                                        'docx': 'docx',
                                        'txt': 'text',
                                        'md': 'text',
                                        'json': 'json',
                                        'csv': 'csv',
                                        'xlsx': 'excel',
                                        'yaml': 'openapi',
                                        'yml': 'openapi',
                                        'mdx': 'mdx',
                                        'xml': 'xml',
                                        'rss': 'rss'
                                    }
                                    source_type = source_type_map.get(ext, 'text')

                                    # Load document using HawkinsRAG
                                    result = rag.load_document(file_path, source_type=source_type)
                                    if result:
                                        logger.info(f"Loaded document: {filename}")
                                    else:
                                        logger.warning(f"Failed to load document: {filename}")
                                except Exception as e:
                                    logger.error(f"Error loading document {filename}: {str(e)}")
                    except Exception as e:
                        logger.error(f"Error accessing RAG documents directory: {str(e)}")
                        raise

            tools = AgentManager._get_tools(
                config['config'].get('tools', []),
                rag_instance=rag if 'RAGTool' in config['config'].get('tools', []) else None
            )

            # Create Hawkins Agent using AgentBuilder
            hawkins_agent = (AgentBuilder(config['name'])
                .with_model(config['config'].get('model', 'openai/gpt-4'))
                .with_provider(
                    LiteLLMProvider,
                    temperature=config['config'].get('temperature', 0.7)
                ))

            # Add tools if specified
            for tool in tools:
                hawkins_agent = hawkins_agent.with_tool(tool)

            # Build the agent
            hawkins_agent = hawkins_agent.build()

            # Create agent metadata
            agent = {
                'id': agent_id,
                'name': config['name'],
                'description': config['description'],
                'type': config.get('type', 'conversation_agent'),
                'config': config['config'],
                'status': 'inactive',
                'deployed': False,
                '_hawkins_agent': hawkins_agent,
                '_rag_instance': rag
            }

            return agent

        except Exception as e:
            logger.error(f"Failed to create agent: {str(e)}")
            raise

    @staticmethod
    async def test_agent(agent: Dict[str, Any], input_data: Any) -> Dict[str, Any]:
        """Test an agent with the given input using Hawkins Agent SDK"""
        try:
            if '_hawkins_agent' not in agent:
                # Create a new agent instance if testing a saved agent
                new_agent = await AgentManager.create_agent({
                    'name': agent['name'],
                    'description': agent['description'],
                    'type': agent['type'],
                    'config': agent['config']
                })
                hawkins_agent = new_agent['_hawkins_agent']
            else:
                hawkins_agent = agent['_hawkins_agent']

            start_time = time.time()
            query = str(input_data)

            try:
                response = await hawkins_agent.process(query)
                logger.debug(f"Raw agent response: {response}")

                # Get the message content
                message = ''
                if isinstance(response, dict):
                    message = response.get('message', '')
                else:
                    message = str(response)

                # Clean any tool preparation text and AgentResponse wrapper
                if 'AgentResponse(' in message:
                    try:
                        # Extract just the message content
                        message = message.split('message="')[1].split('",')[0]

                        # Remove tool preparation text if present
                        if '<tool_call>' in message:
                            parts = message.split('</tool_call>')
                            if len(parts) > 1:
                                # Take only the content after the tool call
                                message = parts[-1].strip()

                        # If message starts with newlines, clean them
                        message = message.lstrip('\n')
                    except Exception as e:
                        logger.error(f"Error cleaning message: {str(e)}")

                # Handle tool calls
                if isinstance(response, dict) and 'tool_calls' in response:
                    tool_outputs = []
                    for tool_call in response['tool_calls']:
                        tool_name = tool_call.get('name')
                        parameters = tool_call.get('parameters', {})

                        tool = next((t for t in hawkins_agent.tools if t.name == tool_name), None)
                        if tool:
                            result = await _execute_tool(tool, parameters)
                            tool_outputs.append({
                                'tool': tool_name,
                                'success': result.get('success', False),
                                'result': result.get('result', None),
                                'error': result.get('error', None)
                            })

                    return {
                        'output': message,  # Just the clean message
                        'response_time': time.time() - start_time,
                        'memory_usage': 0,
                        'metadata': {'tool_results': tool_outputs}
                    }

                return {
                    'output': message,  # Just the clean message
                    'response_time': time.time() - start_time,
                    'memory_usage': 0
                }

            except Exception as e:
                error_msg = f"Error processing query: {str(e)}"
                logger.error(error_msg, exc_info=True)
                return {
                    'output': error_msg,
                    'response_time': time.time() - start_time,
                    'memory_usage': 0
                }

        except Exception as e:
            logger.error(f"Failed to test agent: {str(e)}", exc_info=True)
            raise

    @staticmethod
    async def deploy_agent(agent: Dict[str, Any], deployment_config: Dict[str, Any]) -> bool:
        """Deploy an agent with the given configuration using Hawkins Agent SDK"""
        try:
            hawkins_agent = agent['_hawkins_agent']

            # Configure deployment settings
            deployment_settings = {
                'environment': deployment_config['type'].lower(),
                'resources': deployment_config['resources'],
                'scaling_enabled': deployment_config.get('scaling', False),
                'min_instances': deployment_config.get('min_instances', 1),
                'max_instances': deployment_config.get('max_instances', 1)
            }

            # Deploy using Hawkins Agent SDK
            await hawkins_agent.deploy(**deployment_settings)

            agent['deployed'] = True
            agent['deployment_config'] = deployment_config
            return True

        except Exception as e:
            logger.error(f"Failed to deploy agent: {str(e)}")
            raise

    @staticmethod
    async def get_deployment_status(agent: Dict[str, Any]) -> Dict[str, Any]:
        """Get the deployment status of an agent using Hawkins Agent SDK"""
        try:
            hawkins_agent = agent['_hawkins_agent']
            status = await hawkins_agent.get_status()

            return {
                'status': status.get('state', 'unknown'),
                'instances': status.get('instance_count', 0),
                'uptime': status.get('uptime_hours', 0),
                'logs': status.get('recent_logs', []),
                'cpu_usage': status.get('cpu_metrics', []),
                'memory_usage': status.get('memory_metrics', [])
            }
        except Exception as e:
            logger.error(f"Failed to get deployment status: {str(e)}")
            raise

def resolve_rag_dir(rag_dir: str) -> Optional[str]:
    """Resolve RAG documents directory path"""
    if not rag_dir:
        return None

    # If relative path, make it absolute from current working directory
    if not os.path.isabs(rag_dir):
        rag_dir = os.path.join(os.getcwd(), rag_dir)

    # Verify directory exists
    if not os.path.exists(rag_dir):
        logger.warning(f"RAG documents directory not found: {rag_dir}")
        return None

    return rag_dir

#The extract_agent_response_message function is removed because its logic is now within test_agent


# Export functions for direct use
async def create_agent(config: Dict[str, Any]) -> Dict[str, Any]:
    return await AgentManager.create_agent(config)

async def test_agent(agent: Dict[str, Any], input_data: Any) -> Dict[str, Any]:
    return await AgentManager.test_agent(agent, input_data)

async def deploy_agent(agent: Dict[str, Any], deployment_config: Dict[str, Any]) -> bool:
    return await AgentManager.deploy_agent(agent, deployment_config)

async def get_deployment_status(agent: Dict[str, Any]) -> Dict[str, Any]:
    return await AgentManager.get_deployment_status(agent)