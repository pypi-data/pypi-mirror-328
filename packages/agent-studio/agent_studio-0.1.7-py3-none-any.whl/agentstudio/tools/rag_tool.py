"""RAG Tool implementation for AgentStudio"""
from typing import Dict, Any
import logging
from hawkins_agent.tools import BaseTool
from hawkins_agent.types import ToolResponse
from ..utils.rag_manager import RAGManager

logger = logging.getLogger(__name__)

class AgentStudioRAGTool(BaseTool):
    """Tool for querying knowledge base in AgentStudio"""
    
    def __init__(self, name: str = "RAGTool"):
        """Initialize RAG tool with AgentStudio's RAG manager"""
        super().__init__(name=name)
        self.rag_manager = RAGManager()
        logger.info("AgentStudio RAG Tool initialized")
    
    @property
    def description(self) -> str:
        """Tool description for the agent"""
        return (
            "A tool for querying AgentStudio's knowledge base using RAG "
            "(Retrieval Augmented Generation). Use this to find relevant "
            "information from the loaded documents.\n"
            "Parameters: query (string) - the question to ask the knowledge base"
        )
    
    async def execute(self, **kwargs) -> ToolResponse:
        """Execute RAG query using AgentStudio's RAG manager"""
        try:
            # Extract and validate query
            query = kwargs.get('query', '')
            if not query or not isinstance(query, str):
                return ToolResponse(
                    success=False,
                    result=None,
                    error="Invalid or missing query parameter"
                )
            
            # Process query through RAG manager
            response = await self.rag_manager.process_query(query)
            
            # Convert response to ToolResponse format
            return ToolResponse(
                success=response['success'],
                result=response['result'],
                error=response['error']
            )
            
        except Exception as e:
            error_msg = f"RAG tool execution failed: {str(e)}"
            logger.error(error_msg, exc_info=True)
            return ToolResponse(
                success=False,
                result=None,
                error=error_msg
            )

    async def add_document(self, content: str, metadata: Dict[str, Any] = None) -> ToolResponse:
        """Add a document to the knowledge base"""
        try:
            result = await self.rag_manager.add_document(content, metadata)
            return ToolResponse(
                success=result['success'],
                result=result['result'],
                error=result['error']
            )
        except Exception as e:
            error_msg = f"Failed to add document: {str(e)}"
            logger.error(error_msg, exc_info=True)
            return ToolResponse(
                success=False,
                result=None,
                error=error_msg
            )
