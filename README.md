# Personal AI Assistant CrewAI Project

## Overview
This project implements a sophisticated multi-agent personal AI assistant leveraging the CrewAI framework. It showcases how specialized AI agents can collaboratively work towards complex user goals, enhancing productivity, well-being, and knowledge acquisition. The system is designed with a hybrid memory architecture, combining short-term conversational context with a long-term vector database for persistent learning and recall.

## Project Structure

```
crew-ai/
├── .venv/                # Python virtual environment
├── agents.py             # Defines the roles, goals, and backstories of all AI agents
├── main.py               # Main script to orchestrate the CrewAI agents and tasks
├── memory_tools.py       # Custom tools for the Memory Agent (ChromaDB integration)
├── requirements.txt      # Lists Python dependencies (e.g., crewai)
├── SPECIFICATION.md      # Detailed product vision, architecture, and communication flows
├── tasks.py              # Defines the specific tasks that agents can perform
├── chroma_db/            # Persistent storage for ChromaDB (vector database)
└── .env                  # (Optional) Environment variables, e.g., OPENAI_API_KEY
```

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone git@github.com:vcb88/crew-ai-demo.git
    cd crew-ai-demo/crew-ai
    ```
    *(Note: Assuming the user has already cloned or is in the `crew-ai` directory)*

2.  **Create a Python Virtual Environment:**
    It's highly recommended to use a virtual environment to manage project dependencies.
    ```bash
    python3 -m venv .venv
    ```

3.  **Activate the Virtual Environment:**
    *   On macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```
    *   On Windows:
        ```bash
        .venv\Scripts\activate
        ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure LLM and API Key:**
    This project is configured to use a local LLM (Large Language Model) accessible via an OpenAI-compatible API endpoint (e.g., LM Studio, Ollama).
    *   Ensure your local LLM is running and accessible at `http://192.168.1.14:1234/v1`.
    *   Create a file named `.env` in the `crew-ai/` directory.
    *   Add the following line to the `.env` file:
        ```
        OPENAI_API_KEY='sk-no-key-required'
        ```
        (Note: For local LLMs, `sk-no-key-required` is a common placeholder and usually sufficient.)

6.  **ChromaDB Setup (for Memory Agent):**
    The Memory Agent uses ChromaDB as a local vector database.
    *   Upon first run, a `chroma_db/` directory will be created in the project root to store the database.
    *   The current implementation uses a **mock embedding function** for demonstration purposes. For real-world applications, you would replace this with a robust embedding model (e.g., from OpenAI, Sentence Transformers) to enable meaningful semantic search.

## How to Run

Once setup is complete, you can run the main script:

```bash
python main.py
```
*(Note: This assumes the virtual environment is activated. If not, use `python3 .venv/bin/python main.py`)*

## Running with Docker Compose

For a containerized setup, you can use Docker Compose.

1.  **Ensure Docker is running** on your system.
2.  **Ensure your local LLM is running** and accessible at `http://192.168.1.14:1234/v1`.
3.  **Build and run the services:**
    ```bash
    docker-compose up --build
    ```
    This will build the Docker image for the application and start the container. The ChromaDB data will be persisted in a Docker volume named `chroma_data`.
4.  **To stop the services:**
    ```bash
    docker-compose down
    ```

## Architecture and Communication

Refer to `SPECIFICATION.md` for a detailed overview of the system's architecture, agent roles, and communication flows.

## Roadmap

See `ROADMAP.md` for a detailed roadmap of future features, including effort and impact estimations.

## Demonstration Results

The project successfully executed the "Investment Planning" scenario, demonstrating the collaborative intelligence of the multi-agent system and the effective integration of the Hybrid Memory Agent with a local LLM.

**Key steps demonstrated:**
*   **Deep Research Specialist** successfully researched AI stocks.
*   **Memory Manager** successfully stored and retrieved research findings, explanations, financial advice, and schedules in the ChromaDB vector database.
*   **Personal Tutor** provided explanations based on research.
*   **Financial Advisor** offered financial advice.
*   **Planner** generated a learning schedule.
*   All agents communicated effectively by passing task outputs as context.
*   The system successfully utilized a local LLM (LM Studio) for agent reasoning.

This confirms the core functionality and inter-agent communication mechanisms are working as designed.

---
