# tasks.py
from crewai import Task

# Placeholder tasks for each agent

def plan_user_schedule(agent, description):
    return Task(
        description=description,
        agent=agent,
        expected_output='A detailed schedule or plan.'
    )

def research_topic(agent, topic):
    return Task(
        description=f'Conduct in-depth research on the topic: {topic}',
        agent=agent,
        expected_output='Comprehensive research findings.'
    )

def explain_concept(agent, concept):
    return Task(
        description=f'Explain the concept: {concept} in an easy-to-understand manner.',
        agent=agent,
        expected_output='A clear and concise explanation.'
    )

def provide_financial_advice(agent, advice_request):
    return Task(
        description=f'Provide financial advice regarding: {advice_request}',
        agent=agent,
        expected_output='Actionable financial recommendations.'
    )

def suggest_health_plan(agent, health_goal):
    return Task(
        description=f'Suggest a personalized health and wellness plan for: {health_goal}',
        agent=agent,
        expected_output='A tailored health and wellness plan.'
    )
