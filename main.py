# main.py
from crewai import Crew
from agents import deep_research_agent, tutor_agent, financial_advisor_agent, planner_agent
from tasks import research_topic, explain_concept, provide_financial_advice, plan_user_schedule
from langchain_openai import ChatOpenAI

if __name__ == "__main__":
    print("Starting Personal Assistant CrewAI project...")

    # Define the local LLM
    local_llm = ChatOpenAI(
        model="local-model",
        base_url="http://192.168.1.14:1234/v1",
        api_key="sk-no-key-required"
    )

    # Scenario: User wants to start investing in AI stocks.
    # They need to understand the basics, ensure it fits their budget,
    # and integrate learning into their schedule.

    # Define tasks
    research_ai_stocks_task = research_topic(
        agent=deep_research_agent,
        topic="overview of AI stocks and their potential"
    )

    explain_investment_basics_task = explain_concept(
        agent=tutor_agent,
        concept="basics of stock investment and how to interpret AI stock research"
    )
    # This task will depend on the output of research_ai_stocks_task
    explain_investment_basics_task.context = [research_ai_stocks_task]

    assess_investment_budget_task = provide_financial_advice(
        agent=financial_advisor_agent,
        advice_request="assess user's current budget for a new investment in AI stocks, considering their financial goals and current expenses"
    )
    # This task might also benefit from the research, but primarily focuses on user's finances.
    assess_investment_budget_task.context = [research_ai_stocks_task]


    schedule_learning_task = plan_user_schedule(
        agent=planner_agent,
        description="schedule dedicated time for the user to learn about AI stock investment and review financial advice, suggesting optimal times based on a typical daily routine"
    )
    # This task depends on the output of both explanation and financial advice.
    schedule_learning_task.context = [explain_investment_basics_task, assess_investment_budget_task]


    # Create the crew
    personal_assistant_crew = Crew(
        agents=[
            deep_research_agent,
            tutor_agent,
            financial_advisor_agent,
            planner_agent
        ],
        tasks=[
            research_ai_stocks_task,
            explain_investment_basics_task,
            assess_investment_budget_task,
            schedule_learning_task
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