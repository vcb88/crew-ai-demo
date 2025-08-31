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
    print("Starting Personal Assistant CrewAI project...")

    # Define the local LLM
    local_llm = ChatOpenAI(
        model="local-model",
        base_url="http://192.168.1.14:1234/v1",
        api_key="sk-no-key-required"
    )

    # Assign tools to memory_agent
    memory_agent.tools = [store_memory, retrieve_memory]

    # Scenario: User wants to start investing in AI stocks.
    # They need to understand the basics, ensure it fits their budget,
    # and integrate learning into their schedule.

    # Define tasks
    research_ai_stocks_task = research_topic(
        agent=deep_research_agent,
        topic="overview of AI stocks and their potential"
    )

    # New task: Store research findings in memory
    store_research_memory_task = Task(
        description=dedent(f"""
            Store the research findings from 'research_ai_stocks_task' in memory.
            Use the 'store_memory' tool.
            Memory ID should be 'ai_stocks_research'.
            Metadata should include 'topic': 'AI Stocks', 'source': 'Deep Research Agent'.
            Content to store: {research_ai_stocks_task.output}
        """),
        agent=memory_agent,
        tools=[store_memory],
        expected_output="Confirmation that memory was stored."
    )
    store_research_memory_task.context = [research_ai_stocks_task]


    # New task: Retrieve relevant memories before explaining
    retrieve_tutor_memory_task = Task(
        description=dedent(f"""
            Retrieve any relevant past explanations or learning materials from memory
            that could help in explaining 'basics of stock investment'.
            Use the 'retrieve_memory' tool with query: "basics of stock investment".
        """),
        agent=memory_agent,
        tools=[retrieve_memory],
        expected_output="List of retrieved memories or an empty list if none."
    )

    explain_investment_basics_task = explain_concept(
        agent=tutor_agent,
        concept="basics of stock investment and how to interpret AI stock research"
    )
    explain_investment_basics_task.context = [research_ai_stocks_task, retrieve_tutor_memory_task] # Add retrieved memory context

    # New task: Store explanation in memory
    store_explanation_memory_task = Task(
        description=dedent(f"""
            Store the explanation from 'explain_investment_basics_task' in memory.
            Use the 'store_memory' tool.
            Memory ID should be 'investment_basics_explanation'.
            Metadata should include 'topic': 'Investment Basics', 'source': 'Tutor Agent'.
            Content to store: {explain_investment_basics_task.output}
        """),
        agent=memory_agent,
        tools=[store_memory],
        expected_output="Confirmation that memory was stored."
    )
    store_explanation_memory_task.context = [explain_investment_basics_task]


    assess_investment_budget_task = provide_financial_advice(
        agent=financial_advisor_agent,
        advice_request="assess user's current budget for a new investment in AI stocks, considering their financial goals and current expenses"
    )
    assess_investment_budget_task.context = [research_ai_stocks_task]

    # New task: Store financial advice in memory
    store_financial_advice_memory_task = Task(
        description=dedent(f"""
            Store the financial advice from 'assess_investment_budget_task' in memory.
            Use the 'store_memory' tool.
            Memory ID should be 'financial_advice_ai_stocks'.
            Metadata should include 'topic': 'Financial Advice', 'investment': 'AI Stocks', 'source': 'Financial Advisor Agent'.
            Content to store: {assess_investment_budget_task.output}
        """),
        agent=memory_agent,
        tools=[store_memory],
        expected_output="Confirmation that memory was stored."
    )
    store_financial_advice_memory_task.context = [assess_investment_budget_task]


    schedule_learning_task = plan_user_schedule(
        agent=planner_agent,
        description="schedule dedicated time for the user to learn about AI stock investment and review financial advice, suggesting optimal times based on a typical daily routine"
    )
    schedule_learning_task.context = [explain_investment_basics_task, assess_investment_budget_task]

    # New task: Store schedule in memory
    store_schedule_memory_task = Task(
        description=dedent(f"""
            Store the generated schedule from 'schedule_learning_task' in memory.
            Use the 'store_memory' tool.
            Memory ID should be 'ai_stocks_learning_schedule'.
            Metadata should include 'topic': 'Learning Schedule', 'investment': 'AI Stocks', 'source': 'Planner Agent'.
            Content to store: {schedule_learning_task.output}
        """),
        agent=memory_agent,
        tools=[store_memory],
        expected_output="Confirmation that memory was stored."
    )
    store_schedule_memory_task.context = [schedule_learning_task]


    # Create the crew
    personal_assistant_crew = Crew(
        agents=[
            deep_research_agent,
            tutor_agent,
            financial_advisor_agent,
            planner_agent,
            memory_agent # Add the new memory agent
        ],
        tasks=[
            research_ai_stocks_task,
            store_research_memory_task,
            retrieve_tutor_memory_task,
            explain_investment_basics_task,
            store_explanation_memory_task,
            assess_investment_budget_task,
            store_financial_advice_memory_task,
            schedule_learning_task,
            store_schedule_memory_task
        ],
        verbose=True,
        llm=local_llm
    )

    # Kick off the crew's work
    result = personal_assistant_crew.kickoff()

    print("\n########################")
    print("## Crew's Work Results:")
    print("########################\n")
    print(result)
