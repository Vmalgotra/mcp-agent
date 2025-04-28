# 🛠️ Running an Agent with Google ADK

This guide explains how to set up and run an agent locally using Google’s ADK (Agent Development Kit).

## Prerequisites:
1. Ensure that the MCP server is running on `localhost` at port `8000`. [Link Text](https://github.com/Vmalgotra/MCPAGENT/blob/main/mcp/README.md)
2. Update the `weather_agent/.env` file with the `GOOGLE_API_KEY`. You can get an API key from Google AI Studio at [Google AI Studio](https://aistudio.google.com/apikey).

## 📂 1. Navigate to the Agent Directory

Open your terminal and navigate to the `agent` directory:

cd agent

## 📦 2. Setup a Virtual Environment
Create and activate a Python virtual environment to manage dependencies cleanly:

python3 -m venv .agent
source .agent/bin/activate

## 📥 3. Install Requirements
Install the necessary Python dependencies using pip:

pip install -r requirements.txt

## 🚀 4. Start the ADK Web Server
Run the agent using ADK’s built-in web server:

adk web --port=8001

This will start your agent on http://localhost:8001.
