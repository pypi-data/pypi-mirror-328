"""
Agent templates and configurations
"""
from typing import List, Dict, Any
from agentstudio.utils.agent_manager import AgentManager


def get_agent_templates() -> List[Dict[str, Any]]:
    """Return available Hawkins Agent templates"""
    # Load custom tools
    custom_tools = AgentManager._load_custom_tools()
    custom_tool_names = [tool['name'] for tool in custom_tools]

    # Base templates configuration
    return [
        {
            'id': 'conversation_agent',
            'name': 'Conversation Agent',
            'description': 'Create an interactive conversational agent powered by Hawkins AI',
            'config_schema': {
                'model': {
                    'type': 'select',
                    'options': [
                        'openai/gpt-4o',  # Latest OpenAI model
                        'anthropic/claude-3-sonnet-20240229',  # Latest Anthropic model
                        'grok-2-1212'  # Latest xAI model
                    ],
                    'default': 'openai/gpt-4o'
                },
                'temperature': {
                    'type': 'slider',
                    'min': 0.0,
                    'max': 1.0,
                    'step': 0.1,
                    'default': 0.7
                },
                'memory_config': {
                    'type': 'multiselect',
                    'options': ['Short-term', 'Long-term', 'Semantic'],
                    'default': ['Short-term', 'Semantic']
                },
                'tools': {
                    'type': 'multiselect',
                    'options': [
                        'WebSearchTool',
                        'RAGTool',
                        'SummarizationTool',
                        'WeatherTool'
                    ] + custom_tool_names,  # Add custom tools to options
                    'default': ['WebSearchTool', 'RAGTool']
                },
                'personality': {
                    'type': 'text',
                    'default': 'Professional and helpful'
                }
            }
        },
        {
            'id': 'task_agent',
            'name': 'Task Automation Agent',
            'description': 'Create an agent that automates specific tasks and workflows',
            'config_schema': {
                'model': {
                    'type': 'select',
                    'options': [
                        'openai/gpt-4o',
                        'anthropic/claude-3-sonnet-20240229',
                        'grok-2-1212'
                    ],
                    'default': 'openai/gpt-4o'
                },
                'temperature': {
                    'type': 'slider',
                    'min': 0.0,
                    'max': 1.0,
                    'step': 0.1,
                    'default': 0.5
                },
                'execution_mode': {
                    'type': 'select',
                    'options': ['Sequential', 'Parallel', 'Adaptive'],
                    'default': 'Sequential'
                },
                'tools': {
                    'type': 'multiselect',
                    'options': [
                        'WebSearchTool',
                        'RAGTool',
                        'SummarizationTool',
                        'WeatherTool'
                    ] + custom_tool_names,  # Add custom tools to options
                    'default': ['WebSearchTool', 'RAGTool']
                },
                'memory_config': {
                    'type': 'multiselect',
                    'options': ['Short-term', 'Long-term', 'Semantic'],
                    'default': ['Short-term']
                }
            }
        },
        {
            'id': 'analysis_agent',
            'name': 'Data Analysis Agent',
            'description': 'Create an agent that performs data analysis and generates insights',
            'config_schema': {
                'model': {
                    'type': 'select',
                    'options': [
                        'openai/gpt-4o',
                        'anthropic/claude-3-sonnet-20240229',
                        'grok-2-1212'
                    ],
                    'default': 'openai/gpt-4o'
                },
                'temperature': {
                    'type': 'slider',
                    'min': 0.0,
                    'max': 1.0,
                    'step': 0.1,
                    'default': 0.3
                },
                'data_sources': {
                    'type': 'multiselect',
                    'options': ['CSV', 'JSON', 'Database', 'API'],
                    'default': ['CSV']
                },
                'tools': {
                    'type': 'multiselect',
                    'options': [
                        'WebSearchTool',
                        'RAGTool',
                        'SummarizationTool',
                        'WeatherTool'
                    ] + custom_tool_names,  # Add custom tools to options
                    'default': ['WebSearchTool', 'RAGTool']
                },
                'memory_config': {
                    'type': 'multiselect',
                    'options': ['Short-term', 'Long-term', 'Semantic'],
                    'default': ['Long-term', 'Semantic']
                }
            }
        }
    ]