import os # New import
from crewai import Crew, Task
from agents import deep_research_agent, tutor_agent, financial_advisor_agent, planner_agent, memory_agent
from tasks import research_topic, explain_concept, provide_financial_advice, plan_user_schedule
from langchain_openai import ChatOpenAI
from memory_tools import store_memory, retrieve_memory
from textwrap import dedent
from dotenv import load_dotenv # New import

load_dotenv() # Load environment variables from .env file

# Explicitly set OPENAI_API_KEY for litellm/openai client
os.environ["OPENAI_API_KEY"] = "sk-no-key-required"

if __name__ == "__main__":