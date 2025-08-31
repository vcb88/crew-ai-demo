# Personal AI Assistant CrewAI Project

This project implements a multi-agent personal AI assistant using the CrewAI framework. The system is designed to demonstrate collaborative intelligence among specialized AI agents to assist users with various aspects of their daily lives, including scheduling, learning, financial planning, and health & wellness.

## Project Structure

```
crew-ai/
├── .venv/                # Python virtual environment
├── agents.py             # Defines the roles, goals, and backstories of all AI agents
├── main.py               # Main script to orchestrate the CrewAI agents and tasks
├── requirements.txt      # Lists Python dependencies (e.g., crewai)
├── SPECIFICATION.md      # Detailed product vision, architecture, and communication flows
├── tasks.py              # Defines the specific tasks that agents can perform
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

5.  **Configure API Key:**
    This project requires an OpenAI API key for the agents to function.
    *   Obtain your API key from [platform.openai.com](https://platform.openai.com/).
    *   Create a file named `.env` in the `crew-ai/` directory.
    *   Add your API key to the `.env` file in the following format:
        ```
        OPENAI_API_KEY='your_api_key_here'
        ```
        Replace `'your_api_key_here'` with your actual OpenAI API key.

## How to Run

Once setup is complete, you can run the main script:

```bash
python main.py
```
*(Note: This assumes the virtual environment is activated. If not, use `python3 .venv/bin/python main.py`)*

## Architecture and Communication

Refer to `SPECIFICATION.md` for a detailed overview of the system's architecture, agent roles, and communication flows.

---
