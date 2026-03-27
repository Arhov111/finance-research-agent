from crewai import Agent
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
import os

load_dotenv()

# this is the search tool - lets agents search the web for free
search_tool = DuckDuckGoSearchRun()

# Agent 1 - Researcher
researcher = Agent(
    role="Crypto and Stock Market Researcher",
    goal="Research the latest news, price movements and market sentiment for {asset}",
    backstory="""You are an experienced financial researcher with deep knowledge 
    of both traditional markets and cryptocurrency. You are skilled at finding 
    relevant and accurate market information quickly.""",
    tools=[search_tool],
    verbose=True,
    allow_delegation=False
)

# Agent 2 - Analyst
analyst = Agent(
    role="Financial Analyst",
    goal="Analyze the research data for {asset} and identify key risks and opportunities",
    backstory="""You are a senior financial analyst with expertise in both 
    crypto and traditional markets. You excel at interpreting market data 
    and providing actionable insights.""",
    tools=[search_tool],
    verbose=True,
    allow_delegation=False
)

# Agent 3 - Report Writer
writer = Agent(
    role="Financial Report Writer",
    goal="Write a clear and professional research report for {asset}",
    backstory="""You are a professional financial writer who specializes in 
    making complex financial information accessible and actionable. 
    You write clear, structured reports that investors can act on.""",
    verbose=True,
    allow_delegation=False
)