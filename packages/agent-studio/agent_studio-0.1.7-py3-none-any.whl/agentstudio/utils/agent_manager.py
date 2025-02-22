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
from hawkins_agent.tools import WebSearchTool, RAGTool, SummarizationTool, WeatherTool, BaseTool
from hawkins_rag import HawkinsRAG
from ..tools.rag_tool import AgentStudioRAGTool

logger = logging.getLogger(__name__)

class AgentManager:
    @staticmethod
    def _get_custom_tools_dir() -> str:
        """Get the absolute path to the custom tools directory"""
        return 'custom_tools'

    @staticmethod
    def _load_custom_tools() -> Dict[str, Any]:
        """Load custom tools from the custom_tools directory"""
        custom_tools = {}
        custom_tools_dir = AgentManager._get_custom_tools_dir()

        if not os.path.exists(custom_tools_dir):
            logger.warning(f"Custom tools directory not found: {custom_tools_dir}")
            return custom_tools

        logger.info(f"Loading custom tools from: {custom_tools_dir}")

        for filename in os.listdir(custom_tools_dir):
            if filename.endswith('_meta.json'):
                try:
                    meta_path = os.path.join(custom_tools_dir, filename)
                    py_file = filename.replace('_meta.json', '.py')
                    py_path = os.path.join(custom_tools_dir, py_file)

                    if not os.path.exists(py_path):
                        logger.warning(f"Python file not found for {filename}")
                        continue

                    with open(meta_path, 'r') as f:
                        tool_meta = json.load(f)
                        tool_name = os.path.splitext(filename)[0].replace('_meta', '')
                        tool_meta['file_path'] = py_path
                        custom_tools[tool_name] = tool_meta
                        logger.info(f"Loaded tool metadata for: {tool_name}")

                except Exception as e:
                    logger.error(f"Error loading custom tool {filename}: {str(e)}")

        return custom_tools

    @staticmethod
    def _get_all_available_tools() -> List[str]:
        """Get a list of all available tools (built-in + custom)"""
        built_in_tools = [
            'WebSearchTool',
            'RAGTool', 
            'SummarizationTool',
            'WeatherTool'
        ]

        # Load custom tools from the base directory
        custom_tools_dir = 'custom_tools'
        custom_tools = {}

        if os.path.exists(custom_tools_dir):
            for filename in os.listdir(custom_tools_dir):
                if filename.endswith('_meta.json'):
                    try:
                        with open(os.path.join(custom_tools_dir, filename), 'r') as f:
                            tool_meta = json.load(f)
                            tool_name = os.path.splitext(filename)[0].replace('_meta', '')
                            custom_tools[tool_name] = tool_meta
                            logger.info(f"Found custom tool: {tool_name}")
                    except Exception as e:
                        logger.error(f"Error loading custom tool metadata: {str(e)}")

        # Combine and return all tools
        custom_tool_names = list(custom_tools.keys())
        all_tools = built_in_tools + custom_tool_names
        logger.info(f"Total available tools: {len(all_tools)} ({len(built_in_tools)} built-in, {len(custom_tool_names)} custom)")
        return all_tools

    @staticmethod
    def _load_custom_tool_class(file_path: str) -> Optional[type]:
        """Dynamically load a custom tool class from a Python file"""
        try:
            spec = importlib.util.spec_from_file_location("custom_tool", file_path)
            if spec is None or spec.loader is None:
                raise ImportError(f"Could not load spec for {file_path}")

            module = importlib.util.module_from_spec(spec)
            # Use a unique name for each module to avoid conflicts
            module_name = f"custom_tool_{os.path.basename(file_path)}"
            sys.modules[module_name] = module
            spec.loader.exec_module(module)

            # Find the tool class that inherits from BaseTool
            for item_name in dir(module):
                item = getattr(module, item_name)
                if isinstance(item, type) and issubclass(item, BaseTool) and item != BaseTool:
                    return item

            raise ValueError(f"No BaseTool subclass found in {file_path}")

        except Exception as e:
            logger.error(f"Error loading custom tool class from {file_path}: {str(e)}")
            return None

    @staticmethod
    def _get_tools(tool_names: list, rag_instance: Optional[HawkinsRAG] = None) -> list:
        """Get tool instances based on tool names"""
        # Built-in tool mapping
        tool_map = {
            'WebSearchTool': WebSearchTool,
            'RAGTool': AgentStudioRAGTool,
            'SummarizationTool': SummarizationTool,
            'WeatherTool': WeatherTool
        }

        # Load custom tools
        custom_tools = AgentManager._load_custom_tools()
        tools = []

        for name in tool_names:
            try:
                if name in tool_map:
                    # Initialize built-in tool
                    tool = tool_map[name]()
                    if tool:
                        tools.append(tool)
                        logger.info(f"Successfully initialized built-in tool: {name}")
                elif name.lower() in custom_tools:
                    # Load and initialize custom tool
                    tool_meta = custom_tools[name.lower()]
                    tool_class = AgentManager._load_custom_tool_class(tool_meta['file_path'])

                    if tool_class:
                        tool = tool_class(name=name)
                        tools.append(tool)
                        logger.info(f"Successfully initialized custom tool: {name}")
                    else:
                        logger.warning(f"Failed to load custom tool class: {name}")
                else:
                    logger.warning(f"Unknown tool: {name}")

            except Exception as e:
                logger.error(f"Error initializing tool {name}: {str(e)}")

        return tools

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

            # Handle model configuration
            model = config['config'].get('model')
            if isinstance(model, dict):
                if model.get('type') == 'custom':
                    # Use the custom model string provided by the user
                    model = model.get('value')
                    logger.info(f"Using custom LiteLLM model: {model}")
                else:
                    # If it's a predefined model selection
                    model = model.get('selected', 'openai/gpt-4o')
            else:
                # Default to gpt-4o if no valid model configuration is found
                model = 'openai/gpt-4o'
                logger.info("Using default model: openai/gpt-4o")

            # Create Hawkins Agent using AgentBuilder
            hawkins_agent = (AgentBuilder(config['name'])
                .with_model(model)
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

                # Extract message content from AgentResponse or raw response
                message = ''
                if isinstance(response, dict):
                    # Handle dictionary response
                    if 'message' in response:
                        if isinstance(response['message'], str):
                            message = response['message']
                        elif hasattr(response['message'], 'content'):
                            message = response['message'].content
                        else:
                            message = str(response['message'])
                    else:
                        message = str(response)
                else:
                    # Try to extract message from object attributes
                    if hasattr(response, 'message'):
                        if isinstance(response.message, str):
                            message = response.message
                        elif hasattr(response.message, 'content'):
                            message = response.message.content
                        else:
                            message = str(response.message)
                    else:
                        message = str(response)

                # Handle tool calls if present
                tool_outputs = []
                if isinstance(response, dict) and 'tool_calls' in response:
                    for tool_call in response['tool_calls']:
                        tool_name = tool_call.get('name')
                        parameters = tool_call.get('parameters', {})

                        # Find the tool instance
                        tool = next((t for t in hawkins_agent.tools if t.name == tool_name), None)
                        if tool:
                            try:
                                # Execute the tool
                                if hasattr(tool, '_wrap_sync_query'):
                                    result = await tool._wrap_sync_query(parameters.get('query', ''))
                                elif hasattr(tool.execute, '__await__'):
                                    result = await tool.execute(**parameters)
                                else:
                                    loop = asyncio.get_event_loop()
                                    result = await loop.run_in_executor(None, lambda: tool.execute(**parameters))

                                # Process the tool result
                                if hasattr(result, 'success') and hasattr(result, 'result'):
                                    # Handle ToolResponse objects
                                    tool_result = {
                                        'tool': tool_name,
                                        'success': result.success,
                                        'result': result.result.message if hasattr(result.result, 'message') else str(result.result),
                                        'error': result.error if result.error else None
                                    }
                                else:
                                    # Handle raw results
                                    tool_result = {
                                        'tool': tool_name,
                                        'success': True,
                                        'result': str(result),
                                        'error': None
                                    }
                                tool_outputs.append(tool_result)
                            except Exception as e:
                                tool_outputs.append({
                                    'tool': tool_name,
                                    'success': False,
                                    'result': None,
                                    'error': str(e)
                                })

                return {
                    'output': message,
                    'response_time': time.time() - start_time,
                    'memory_usage': 0,
                    'tool_outputs': tool_outputs if tool_outputs else None
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

    @staticmethod
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

# Export functions for direct use
async def create_agent(config: Dict[str, Any]) -> Dict[str, Any]:
    return await AgentManager.create_agent(config)

async def test_agent(agent: Dict[str, Any], input_data: Any) -> Dict[str, Any]:
    return await AgentManager.test_agent(agent, input_data)

async def deploy_agent(agent: Dict[str, Any], deployment_config: Dict[str, Any]) -> bool:
    return await AgentManager.deploy_agent(agent, deployment_config)

async def get_deployment_status(agent: Dict[str, Any]) -> Dict[str, Any]:
    return await AgentManager.get_deployment_status(agent)