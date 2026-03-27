from crewai import Agent
from crewai.tools import BaseTool
from crewai_tools import ScrapeWebsiteTool, WebsiteSearchTool
from dotenv import load_dotenv
import os
from pydantic import Field
from ddgs import DDGS

load_dotenv()

class DuckDuckGoTool(BaseTool):
    name: str = "DuckDuckGo Search"
    description: str = "Search the web for current information about stocks and crypto"

    def _run(self, query: str) -> str:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))
            return "\n".join([r['title'] + ": " + r['body'] for r in results])

search_tool = DuckDuckGoTool()

researcher = Agent(
    role="Crypto and Stock Market Researcher",
    goal="Research the latest news, price movements and market sentiment for {asset}",
    backstory="""You are an experienced financial researcher with deep knowledge 
    of both traditional markets and cryptocurrency.""",
    tools=[search_tool],
    verbose=True,
    allow_delegation=False
)

analyst = Agent(
    role="Financial Analyst",
    goal="Analyze the research data for {asset} and identify key risks and opportunities",
    backstory="""You are a senior financial analyst with expertise in both 
    crypto and traditional markets.""",
    tools=[search_tool],
    verbose=True,
    allow_delegation=False
)

writer = Agent(
    role="Financial Report Writer",
    goal="Write a clear and professional research report for {asset}",
    backstory="""You are a professional financial writer who specializes in 
    making complex financial information accessible and actionable.""",
    verbose=True,
    allow_delegation=False
)
