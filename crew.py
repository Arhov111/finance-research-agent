from crewai import Crew, Process, LLM
from agents import researcher, analyst, writer
from tasks import research_task, analysis_task, write_task
import os
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

researcher.llm = llm
analyst.llm = llm
writer.llm = llm

def run_research(asset):
    crew = Crew(
        agents=[researcher, analyst, writer],
        tasks=[research_task, analysis_task, write_task],
        process=Process.sequential,
        verbose=True
    )
    result = crew.kickoff(inputs={"asset": asset})
    return result
