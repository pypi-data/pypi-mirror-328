"""
ArXiv search tool for finding research papers
"""
from typing import Dict, Any, List
import requests
import xml.etree.ElementTree as ET

class CustomTool:
    def __init__(self, name: str):
        self.name = name
        self.base_url = "http://export.arxiv.org/api/query"
    
    async def execute(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Execute ArXiv search"""
        try:
            query = parameters.get("query", "")
            max_results = parameters.get("max_results", 5)
            
            # Make API request
            response = requests.get(
                self.base_url,
                params={
                    "search_query": query,
                    "max_results": max_results
                }
            )
            response.raise_for_status()
            
            # Parse XML response
            root = ET.fromstring(response.text)
            
            # Extract paper information
            papers = []
            for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
                paper = {
                    "title": entry.find("{http://www.w3.org/2005/Atom}title").text.strip(),
                    "authors": [author.find("{http://www.w3.org/2005/Atom}name").text 
                               for author in entry.findall("{http://www.w3.org/2005/Atom}author")],
                    "summary": entry.find("{http://www.w3.org/2005/Atom}summary").text.strip(),
                    "link": entry.find("{http://www.w3.org/2005/Atom}id").text
                }
                papers.append(paper)
            
            return {
                "success": True,
                "result": papers
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
