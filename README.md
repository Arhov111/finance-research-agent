# 📈 Finance & Crypto Research Agent

An AI-powered multi-agent system that automatically researches stocks and cryptocurrencies and generates professional investment research reports.

## Overview

This application uses three specialized AI agents working together to research any stock or cryptocurrency and produce a structured investment report with current market data, opportunities, risks, and sentiment analysis.

## How It Works
```
User enters asset (e.g. "Bitcoin" or "NVIDIA")
        ↓
Agent 1 — Researcher: searches the web for latest news and price data
        ↓
Agent 2 — Analyst: identifies key risks and opportunities
        ↓
Agent 3 — Report Writer: produces a professional investment report
        ↓
Report displayed in Streamlit web interface
```

## Features

- Real-time web search for current market data
- Multi-agent architecture with specialized roles
- Professional report generation with executive summary
- Supports any stock or cryptocurrency
- Clean Streamlit web interface

## Tech Stack

- Python
- CrewAI — multi-agent orchestration
- Groq (Llama 3.3) — LLM inference
- DuckDuckGo Search — real-time web search
- Streamlit — web interface
- LangChain — search tool integration

## Setup

1. Clone the repository
```bash
git clone https://github.com/Arhov111/finance-research-agent.git
cd finance-research-agent
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install crewai crewai-tools streamlit python-dotenv langchain-community duckduckgo-search litellm ddgs
```

4. Create .env file
```
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=fake-key
```

5. Run the app
```bash
python -m streamlit run app.py
```

## Project Structure
```
finance_research_agent/
├── agents.py      # Three specialized AI agents
├── tasks.py       # Tasks assigned to each agent
├── crew.py        # Crew orchestration and LLM config
├── app.py         # Streamlit web interface
├── .env           # API keys (not tracked by git)
└── .gitignore
```

## Example Output

Enter any asset like:
- Bitcoin
- NVIDIA
- Apple
- Ethereum
- Tesla

The system will generate a full research report including executive summary, current market status, key findings, opportunities, risks, and sentiment outlook.

## Author

Araks Hovhannisyan
