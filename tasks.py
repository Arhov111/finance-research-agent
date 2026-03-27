from crewai import Task
from agents import researcher, analyst, writer

# Task 1 - Research
research_task = Task(
    description="""
    Research the following asset: {asset}
    
    Find and gather:
    1. Current price and recent price movements
    2. Latest news from the past week
    3. Market sentiment (what are people saying?)
    4. Any major recent events affecting this asset
    5. Trading volume and market cap if available
    
    Be thorough and find real current information.
    """,
    expected_output="""
    A comprehensive research summary including:
    - Current price and price movements
    - Key news from the past week
    - Market sentiment overview
    - Major events or catalysts
    """,
    agent=researcher
)

# Task 2 - Analysis
analysis_task = Task(
    description="""
    Using the research gathered about {asset}, provide a thorough analysis:
    
    1. Identify the top 3 opportunities
    2. Identify the top 3 risks
    3. Assess overall market sentiment (Bullish/Neutral/Bearish)
    4. Give a short term outlook (next 30 days)
    """,
    expected_output="""
    A structured analysis including:
    - Top opportunities
    - Top risks  
    - Sentiment assessment
    - Short term outlook
    """,
    agent=analyst,
    context=[research_task]  # analyst reads researcher's output first
)

# Task 3 - Write Report
write_task = Task(
    description="""
    Using the research and analysis about {asset}, write a professional 
    investment research report.
    
    The report must include:
    - Executive Summary
    - Current Market Status
    - Key Findings
    - Opportunities
    - Risks
    - Sentiment & Outlook
    - Disclaimer
    
    Make it professional, clear and actionable.
    """,
    expected_output="""
    A complete professional research report in markdown format
    with all sections clearly labeled.
    """,
    agent=writer,
    context=[research_task, analysis_task]  # writer reads both outputs
)