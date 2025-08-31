# Personal AI Assistant System Specification

## 1. Product Vision and Goal
To develop an intelligent, multi-agent personal AI assistant capable of proactively managing various aspects of a user's life, including scheduling, learning, financial planning, and health & wellness, through seamless inter-agent communication and collaboration. The primary goal is to enhance user productivity, well-being, and knowledge acquisition.

## 2. Core Features
Based on the selected agents, the system will provide the following core functionalities:
*   **Intelligent Scheduling & Planning:** Manage calendars, appointments, and tasks.
*   **In-depth Information Retrieval:** Conduct comprehensive research on diverse topics.
*   **Personalized Learning & Explanation:** Simplify complex concepts and adapt to learning styles.
*   **Financial Management & Advice:** Track expenses, manage budgets, and provide investment insights.
*   **Health & Wellness Guidance:** Suggest routines, meal plans, and mindfulness practices.

## 3. Agent Roles and Responsibilities

### 3.1. Planner Agent
*   **Role:** Manages the user's schedule, appointments, and tasks.
*   **Responsibilities:**
    *   Integrate tasks and appointments into daily, weekly, and monthly schedules.
    *   Optimize schedules for productivity and well-being.
    *   Receive scheduling requests from other agents (e.g., "schedule a learning session," "block time for a workout").
    *   Communicate schedule conflicts or confirmations.

### 3.2. Deep Research Agent
*   **Role:** Conducts thorough and in-depth research on any given topic.
*   **Responsibilities:**
    *   Receive research queries from other agents or the user.
    *   Gather, synthesize, and structure information from various sources.
    *   Provide comprehensive and relevant insights.
    *   Communicate research findings to requesting agents.

### 3.3. Tutor Agent
*   **Role:** Explains complex concepts in an understandable and engaging manner.
*   **Responsibilities:**
    *   Receive requests to explain concepts, often based on research findings.
    *   Adapt explanations to the user's presumed learning style.
    *   Break down intricate subjects into simpler terms.
    *   Communicate clear and concise explanations.

### 3.4. Financial Advisor Agent
*   **Role:** Provides sound financial advice, manages budgets, tracks expenses, and identifies investment opportunities.
*   **Responsibilities:**
    *   Receive financial queries or data from the user or other agents.
    *   Analyze financial data (e.g., budget, expenses, investment goals).
    *   Provide actionable financial recommendations.
    *   Communicate financial assessments and advice.

### 3.5. Health & Wellness Coach Agent
*   **Role:** Guides the user towards a healthier lifestyle.
*   **Responsibilities:**
    *   Receive health-related goals or data from the user.
    *   Suggest personalized fitness routines, meal plans, and mindfulness practices.
    *   Provide motivational support and track progress.
    *   Communicate health and wellness plans and recommendations.

## 4. Architecture Overview (High-Level)

The Personal AI Assistant system will be built upon the CrewAI framework, leveraging a multi-agent architecture. Each agent operates semi-autonomously with a defined role, goal, and backstory, but critically, they communicate and collaborate to achieve complex user requests.

*   **Central Orchestration (CrewAI):** A main script (`main.py`) will define the overall "Crew" and initiate tasks. It will manage the flow of information and task delegation among agents.
*   **Agent Modules:** Each agent will be defined in `agents.py`, encapsulating its specific capabilities.
*   **Task Modules:** Specific tasks that agents can perform will be defined in `tasks.py`.
*   **Communication Channels:** Agents will communicate by passing the output of one task as context to another task, enabling a sequential and collaborative workflow.

## 5. Communication Flow Examples

### Example 1: Investment Planning
1.  **User Request:** "I want to start investing in AI stocks. Help me understand it, see if I can afford it, and schedule time to learn."
2.  **Deep Research Agent:** Receives a task to research "overview of AI stocks and their potential."
    *   *Output:* Comprehensive research report on AI stocks.
3.  **Tutor Agent:** Receives a task to "explain the basics of stock investment and how to interpret AI stock research."
    *   *Input:* Output from Deep Research Agent.
    *   *Output:* Simplified explanation of stock investment and AI stock research.
4.  **Financial Advisor Agent:** Receives a task to "assess user's current budget for a new investment in AI stocks."
    *   *Input:* Output from Deep Research Agent (for context on AI stocks) and potentially user's financial data (simulated).
    *   *Output:* Financial assessment and advice on affordability.
5.  **Planner Agent:** Receives a task to "schedule dedicated time for the user to learn about AI stock investment and review financial advice."
    *   *Input:* Output from Tutor Agent (learning content) and Financial Advisor Agent (advice).
    *   *Output:* Proposed schedule for learning and review sessions.

### Example 2: Healthy Lifestyle Integration
1.  **User Request:** "I want to start a healthier lifestyle. Can you suggest a plan and help me fit it into my week?"
2.  **Health & Wellness Coach Agent:** Receives a task to "suggest a personalized health and wellness plan."
    *   *Output:* Detailed plan including workout routines, meal suggestions, and mindfulness exercises.
3.  **Planner Agent:** Receives a task to "integrate the health and wellness plan into the user's weekly schedule."
    *   *Input:* Output from Health & Wellness Coach Agent.
    *   *Output:* Updated weekly schedule with health activities.

## 6. Tools and Dependencies
*   **Core Framework:** CrewAI
*   **Python Libraries:** (as specified in `requirements.txt`, e.g., `crewai`, `openai` for LLM integration)
*   **LLM Provider:** An external Large Language Model (e.g., OpenAI GPT models, Google Gemini) will be required for agents to perform their reasoning and task execution. API keys will need to be configured.
*   **Potential Future Tools (for enhanced functionality):**
    *   Calendar API (for Planner)
    *   Search API (for Deep Research)
    *   Financial Data API (for Financial Advisor)
    *   Health Tracking API (for Health & Wellness Coach)
