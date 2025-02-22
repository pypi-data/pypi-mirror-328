"""
HawkinsAgent integration package
"""
from typing import Dict, Any, List, Optional
from .agent import AgentBuilder, Message
from .mock import KnowledgeBase, Document
from .llm import LiteLLMProvider
from .tools import WebSearchTool, RAGTool, SummarizationTool, WeatherTool

__all__ = [
    'AgentBuilder',
    'Message',
    'KnowledgeBase',
    'Document',
    'LiteLLMProvider',
    'WebSearchTool',
    'RAGTool',
    'SummarizationTool',
    'WeatherTool'
]
