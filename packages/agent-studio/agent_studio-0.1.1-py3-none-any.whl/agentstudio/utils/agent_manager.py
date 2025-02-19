"""
Agent management utilities for AgentStudio
"""
import uuid
from typing import Dict, Any, List
import time
import asyncio
import os
import json
import importlib.util
import sys
import logging
from hawkins_agent import AgentBuilder, Message
from hawkins_agent.mock import KnowledgeBase, Document
from hawkins_agent.llm import LiteLLMProvider
from hawkins_agent.tools import WebSearchTool, RAGTool, SummarizationTool, WeatherTool

# Set up logging
logger = logging.getLogger(__name__)

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
    def _get_tools(tool_names: list, knowledge_base: KnowledgeBase = None) -> list:
        """Get tool instances based on tool names"""
        # Previous tool map remains
        tool_map = {
            'WebSearchTool': WebSearchTool,
            'RAGTool': lambda: RAGTool(knowledge_base=knowledge_base) if knowledge_base else None,
            'SummarizationTool': SummarizationTool,
            'WeatherTool': WeatherTool
        }

        # Load custom tools
        custom_tools_dir = 'custom_tools'
        if os.path.exists(custom_tools_dir):
            for tool_name in tool_names:
                tool_file = os.path.join(custom_tools_dir, f"{tool_name.lower()}.py")
                meta_file = os.path.join(custom_tools_dir, f"{tool_name.lower()}_meta.json")

                if os.path.exists(tool_file) and os.path.exists(meta_file):
                    try:
                        # Load tool metadata
                        with open(meta_file, 'r') as f:
                            tool_meta = json.load(f)

                        # Import the custom tool module
                        spec = importlib.util.spec_from_file_location(tool_name, tool_file)
                        module = importlib.util.module_from_spec(spec)
                        sys.modules[tool_name] = module
                        spec.loader.exec_module(module)

                        # Get the tool class and create a factory function
                        tool_class = getattr(module, 'CustomTool')

                        def create_tool(tool_meta=tool_meta):
                            tool = tool_class(name=tool_meta['name'])
                            # Apply any additional configuration from metadata
                            return tool

                        tool_map[tool_name] = create_tool
                    except Exception as e:
                        logger.error(f"Error loading custom tool {tool_name}: {str(e)}")

        tools = []
        for name in tool_names:
            if name in tool_map:
                tool = tool_map[name]() if callable(tool_map[name]) else tool_map[name]
                if tool:
                    tools.append(tool)
        return tools

    @staticmethod
    async def create_agent(config: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new agent with the given configuration using Hawkins Agent SDK"""
        try:
            agent_id = str(uuid.uuid4())

            # Initialize knowledge base
            kb = KnowledgeBase()

            # Load documents for RAG if provided
            rag_documents_dir = config['config'].get('rag_documents_dir')
            if rag_documents_dir and os.path.exists(rag_documents_dir):
                try:
                    for filename in os.listdir(rag_documents_dir):
                        file_path = os.path.join(rag_documents_dir, filename)
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            # Create Document object and add to knowledge base
                            doc = Document(content)
                            await kb.add_document(doc)
                        logger.info(f"Loaded document: {filename}")
                except Exception as e:
                    logger.error(f"Error loading documents: {str(e)}")
                    raise

            # Get selected tools with knowledge base for RAG
            tools = AgentManager._get_tools(
                config['config'].get('tools', []),
                knowledge_base=kb if 'RAGTool' in config['config'].get('tools', []) else None
            )

            # Get memory configuration
            memory_config = AgentManager._get_memory_config(
                config['config'].get('memory_config', ['Short-term'])
            )

            # Create Hawkins Agent using AgentBuilder
            hawkins_agent = (AgentBuilder(config['name'])
                .with_model(config['config'].get('model', 'openai/gpt-4o'))
                .with_provider(
                    LiteLLMProvider,
                    temperature=config['config'].get('temperature', 0.7)
                )
                .with_knowledge_base(kb))

            # Add tools if specified
            for tool in tools:
                hawkins_agent = hawkins_agent.with_tool(tool)

            # Add memory configuration
            hawkins_agent = hawkins_agent.with_memory(memory_config)

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
                '_hawkins_agent': hawkins_agent
            }

            return agent

        except Exception as e:
            logger.error(f"Failed to create agent: {str(e)}")
            raise

    @staticmethod
    def _get_memory_config(memory_types: list) -> Dict[str, Any]:
        """Convert memory type selections to config"""
        config = {
            'retention_days': 30,  # Default retention
            'memory_types': []
        }

        if 'Short-term' in memory_types:
            config['memory_types'].append('short_term')
        if 'Long-term' in memory_types:
            config['memory_types'].append('long_term')
            config['retention_days'] = 90  # Longer retention for long-term memory
        if 'Semantic' in memory_types:
            config['memory_types'].append('semantic')

        return config

    @staticmethod
    async def test_agent(agent: Dict[str, Any], input_data: Any) -> Dict[str, Any]:
        """Test an agent with the given input using Hawkins Agent SDK"""
        try:
            # Create a new Hawkins agent instance if testing a saved agent
            if '_hawkins_agent' not in agent:
                # Initialize knowledge base
                kb = KnowledgeBase()

                # Load documents for RAG if provided
                rag_documents_dir = agent['config'].get('rag_documents_dir')
                if rag_documents_dir and os.path.exists(rag_documents_dir):
                    try:
                        for filename in os.listdir(rag_documents_dir):
                            file_path = os.path.join(rag_documents_dir, filename)
                            with open(file_path, 'r', encoding='utf-8') as f:
                                content = f.read()
                                # Create Document object and add to knowledge base
                                doc = Document(content)
                                await kb.add_document(doc)
                    except Exception as e:
                        logger.error(f"Error loading documents: {str(e)}")
                        raise

                # Get selected tools with knowledge base for RAG
                tools = AgentManager._get_tools(
                    agent['config'].get('tools', []),
                    knowledge_base=kb if 'RAGTool' in agent['config'].get('tools', []) else None
                )

                # Create Hawkins Agent using AgentBuilder
                hawkins_agent = (AgentBuilder(agent['name'])
                    .with_model(agent['config'].get('model', 'openai/gpt-4'))
                    .with_provider(
                        LiteLLMProvider,
                        temperature=agent['config'].get('temperature', 0.7)
                    )
                    .with_knowledge_base(kb))

                # Add tools if specified
                for tool in tools:
                    hawkins_agent = hawkins_agent.with_tool(tool)

                # Build the agent
                hawkins_agent = hawkins_agent.build()
            else:
                hawkins_agent = agent['_hawkins_agent']

            start_time = time.time()

            # Process input directly as string
            query = str(input_data)
            response = await hawkins_agent.process(query)

            end_time = time.time()
            response_time = end_time - start_time

            # Extract response content
            output = None
            if hasattr(response, 'message'):
                if isinstance(response.message, str):
                    output = response.message
                elif hasattr(response.message, 'content'):
                    output = str(response.message.content)
                else:
                    output = str(response.message)
            else:
                output = str(response)

            # Build result dictionary
            result = {
                'output': output,
                'response_time': response_time,
                'memory_usage': 0
            }

            # Process tool calls if available
            if hasattr(response, 'tool_calls') and response.tool_calls:
                result['tool_calls'] = []
                for call in response.tool_calls:
                    try:
                        tool_call = {
                            'name': str(call.get('name', '')),
                            'parameters': str(call.get('parameters', {}))
                        }
                        result['tool_calls'].append(tool_call)
                    except Exception as e:
                        logger.warning(f"Failed to process tool call: {str(e)}")

            # Process tool results if available
            if hasattr(response, 'metadata') and 'tool_results' in response.metadata:
                result['tool_results'] = []
                for res in response.metadata['tool_results']:
                    try:
                        tool_result = {
                            'success': bool(res.get('success', False)),
                            'result': str(res.get('result', '')),
                            'error': str(res.get('error', '')) if not res.get('success', False) else ''
                        }
                        result['tool_results'].append(tool_result)
                    except Exception as e:
                        logger.warning(f"Failed to process tool result: {str(e)}")

            return result

        except Exception as e:
            logger.error(f"Failed to test agent: {str(e)}")
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

# Export functions for direct use
async def create_agent(config: Dict[str, Any]) -> Dict[str, Any]:
    return await AgentManager.create_agent(config)

async def test_agent(agent: Dict[str, Any], input_data: Any) -> Dict[str, Any]:
    return await AgentManager.test_agent(agent, input_data)

async def deploy_agent(agent: Dict[str, Any], deployment_config: Dict[str, Any]) -> bool:
    return await AgentManager.deploy_agent(agent, deployment_config)

async def get_deployment_status(agent: Dict[str, Any]) -> Dict[str, Any]:
    return await AgentManager.get_deployment_status(agent)