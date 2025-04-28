🛠️ Running an Agent with Google ADK
This guide explains how to set up and run an agent locally using Google’s ADK (Agent Development Kit).

Prequisites: 
1. Ensure MCP server is running on localhost port 8000
2. Update weather_agent/.env with the GOOGLE_API_KEY. Get an API key from Google AI Studio (https://aistudio.google.com/apikey).


📂 1. Navigate to the MCP Server Directory: 
cd agent

📦 2. Setup a Virtual Environment:
Create and activate a Python virtual environment to manage dependencies cleanly.

python3 -m venv .agent;
source .agent/bin/activate

📥 3. Install Requirements:
pip install -r requirements.txt

🚀 3. Start the ADK Web Server:
Run the agent using ADK’s built-in web server:
adk web --port=8001

This will start your agent on http://localhost:8001.