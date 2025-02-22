from hawkins_agent.tools import BaseTool
from hawkins_agent.types import ToolResponse
from typing import Dict, Any

class CustomTool(BaseTool):
    """A tool that reverses input text"""

    def __init__(self, name: str):
        """Initialize your tool"""
        super().__init__(name=name)

    @property
    def description(self) -> str:
        """Tool description used by the agent"""
        return "A tool that reverses any input text string"

    def validate_params(self, params: Dict[str, Any]) -> bool:
        """Validate input parameters"""
        if 'query' not in params:
            return False
        if not isinstance(params['query'], str):
            return False
        return True

    async def execute(self, **kwargs) -> ToolResponse:
        """Execute the tool's functionality"""
        try:
            query = kwargs.get('query', '')
            # Reverse the input text
            reversed_text = query[::-1]
            return ToolResponse(
                success=True,
                result=reversed_text,
                error=None
            )
        except Exception as e:
            return ToolResponse(
                success=False,
                result=None,
                error=str(e)
            )