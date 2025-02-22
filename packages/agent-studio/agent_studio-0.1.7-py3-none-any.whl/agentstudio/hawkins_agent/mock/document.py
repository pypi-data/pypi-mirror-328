"""
Mock document implementation
"""
from typing import Dict, Any

class Document:
    """Simple document implementation"""
    
    def __init__(self, content: str, metadata: Dict[str, Any] = None):
        self.content = content
        self.metadata = metadata or {}
        
    def __str__(self) -> str:
        return self.content
