"""RAG functionality manager for AgentStudio"""
from typing import Dict, Any, Optional
import logging
import asyncio
from hawkins_rag import HawkinsRAG
from hawkins_agent.types import ToolResponse

logger = logging.getLogger(__name__)

class RAGManager:
    """Manager class for RAG operations in AgentStudio"""
    
    def __init__(self):
        """Initialize RAG manager"""
        self.kb = HawkinsRAG()
        logger.info("RAG Manager initialized")

    async def process_query(self, query: str) -> Dict[str, Any]:
        """Process a RAG query with proper async handling"""
        try:
            logger.info(f"Processing RAG query: {query}")
            
            # Handle async/sync query execution
            if hasattr(self.kb.query, '__await__'):
                response = await self.kb.query(query)
            else:
                loop = asyncio.get_event_loop()
                response = await loop.run_in_executor(None, self.kb.query, query)
            
            logger.debug(f"Raw RAG response: {response}")
            
            # Standardize response format
            if isinstance(response, dict):
                result = str(response.get('response', response))
            else:
                result = str(response)
            
            return {
                'success': True,
                'result': result,
                'error': None,
                'metadata': {
                    'source': 'rag_knowledge_base',
                    'query': query,
                    'response_type': type(response).__name__
                }
            }
            
        except Exception as e:
            error_msg = f"RAG query processing failed: {str(e)}"
            logger.error(error_msg, exc_info=True)
            return {
                'success': False,
                'result': None,
                'error': error_msg,
                'metadata': {
                    'source': 'rag_knowledge_base',
                    'query': query
                }
            }

    async def add_document(self, content: str, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Add a document to the knowledge base"""
        try:
            if hasattr(self.kb.add_document, '__await__'):
                await self.kb.add_document(content, metadata)
            else:
                loop = asyncio.get_event_loop()
                await loop.run_in_executor(None, self.kb.add_document, content, metadata)
            
            logger.info("Document added successfully to knowledge base")
            return {
                'success': True,
                'result': "Document added successfully",
                'error': None
            }
            
        except Exception as e:
            error_msg = f"Failed to add document: {str(e)}"
            logger.error(error_msg, exc_info=True)
            return {
                'success': False,
                'result': None,
                'error': error_msg
            }
