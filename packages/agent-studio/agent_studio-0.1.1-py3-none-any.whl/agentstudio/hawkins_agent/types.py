"""Type definitions for Hawkins Agent"""
from enum import Enum
from typing import Dict, Any, Optional

class MessageRole(Enum):
    """Enumeration of possible message roles"""
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"

class Message:
    """Message class for agent communication"""
    def __init__(
        self,
        role: MessageRole,
        content: str,
        metadata: Optional[Dict[str, Any]] = None
    ):
        self.role = role
        self.content = content
        self.metadata = metadata or {}

    def to_dict(self) -> Dict[str, Any]:
        """Convert message to dictionary format"""
        return {
            'role': self.role.value,
            'content': self.content,
            'metadata': self.metadata
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Message':
        """Create message from dictionary"""
        return cls(
            role=MessageRole(data['role']),
            content=data['content'],
            metadata=data.get('metadata', {})
        )
