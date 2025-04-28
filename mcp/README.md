# 🛠️ Running the MCP Server

This guide explains how to set up and start the MCP server locally on your machine.

## 📂 1. Navigate to the MCP Server Directory

Open your terminal and navigate to the `mcp_server` directory:

cd mcp_server

## 📦 2. Set Up a Virtual Environment
Create and activate a Python virtual environment to isolate dependencies:

python3 -m venv .mcp
source .mcp/bin/activate

## 📥 3. Install Project Requirements
Install all necessary Python dependencies using pip:

pip install -r requirements.txt

## 🚀 4. Start the MCP Server
Run the server by executing the entrypoint script:

python3 src/weather.py

This will start your MCP server locally, and Uvicorn will be running on http://0.0.0.0:8000.
