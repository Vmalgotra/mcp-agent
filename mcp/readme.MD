🛠️ Running the MCP Server
This guide explains how to set up and start the MCP server locally.

📂 1. Navigate to the MCP Server Directory
cd mcp_server

📦 2. Set Up a Virtual Environment
Create and activate a Python virtual environment:

python3 -m venv .mcp;
source .mcp/bin/activate

📥 3. Install Project Requirements
Install all necessary Python dependencies:

pip install -r requirements.txt

🚀 4. Start the MCP Server
Run the server by executing the entrypoint script:

gstpython3 src/weather.py

This will start your MCP server locally.
Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
