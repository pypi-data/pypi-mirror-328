"""
Mock knowledge base implementation
"""
from typing import List, Any
from .document import Document

class KnowledgeBase:
    """Simple in-memory knowledge base implementation"""
    
    def __init__(self):
        self.documents = []
        
    async def add_document(self, document: Document) -> None:
        """Add a document to the knowledge base"""
        self.documents.append(document)
        
    async def search(self, query: str) -> List[Document]:
        """Search documents (mock implementation)"""
        return self.documents
        
    async def clear(self) -> None:
        """Clear all documents"""
        self.documents = []
