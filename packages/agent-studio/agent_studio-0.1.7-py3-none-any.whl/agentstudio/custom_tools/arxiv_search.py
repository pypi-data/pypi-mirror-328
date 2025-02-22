from hawkins_agent.tools import BaseTool
from hawkins_agent.types import ToolResponse
from typing import Dict, Any, List, Optional
from pathlib import Path
import json

try:
    import arxiv
except ImportError:
    raise ImportError("`arxiv` not installed. Please install using `pip install arxiv`")

try:
    from pypdf import PdfReader
except ImportError:
    raise ImportError("`pypdf` not installed. Please install using `pip install pypdf`")


class CustomTool(BaseTool):
    """Custom tool for searching arxiv papers"""
    
    def __init__(self, name: str = "arxiv_search"):
        """Initialize the arxiv search tool"""
        super().__init__(name=name)
        self.client = arxiv.Client()
        
    @property
    def description(self) -> str:
        """Tool description used by the agent"""
        return (
            "A tool to search arXiv for papers and return the top articles. "
            "Parameters: query (string) - search query, "
            "num_articles (optional int) - number of articles to return (default: 10)"
        )
        
    def validate_params(self, params: Dict[str, Any]) -> bool:
        """Validate input parameters"""
        if not params.get("query"):
            return False
            
        if not isinstance(params["query"], str):
            return False
            
        if "num_articles" in params:
            if not isinstance(params["num_articles"], int) or params["num_articles"] <= 0:
                return False
                
        return True
        
    async def execute(self, **kwargs) -> ToolResponse:
        """Execute the arxiv search"""
        try:
            query = kwargs["query"]
            num_articles = kwargs.get("num_articles", 10)
            
            articles = []
            for result in self.client.results(
                search=arxiv.Search(
                    query=query,
                    max_results=num_articles,
                    sort_by=arxiv.SortCriterion.Relevance,
                    sort_order=arxiv.SortOrder.Descending,
                )
            ):
                try:
                    article = {
                        "title": result.title,
                        "id": result.get_short_id(),
                        "authors": [author.name for author in result.authors],
                        "pdf_url": result.pdf_url,
                        "summary": result.summary,
                    }
                    articles.append(article)
                except Exception as e:
                    return ToolResponse(
                        success=False,
                        result=None,
                        error=f"Error processing article: {str(e)}"
                    )

            return ToolResponse(
                success=True,
                result=articles,  # Return the list directly, not JSON string
                error=None
            )
            
        except Exception as e:
            return ToolResponse(
                success=False,
                result=None,
                error=str(e)
            )