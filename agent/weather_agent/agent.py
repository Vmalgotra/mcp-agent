from google.adk.tools.mcp_tool import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseServerParams
from google.adk.agents import Agent

mcp_toolset = MCPToolset(
    connection_params=SseServerParams(
        url="http://localhost:8000/sse"
    )
)

root_agent = Agent(
    name="weather_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about weather."
    ),
    instruction="""
        You are a helpful weather assistant that can provide weather information and alerts.
        You have access to the following tools:
        - get_weather_alerts: Get weather alerts for a US state using the two-letter state code (e.g. CA, NY)
        - get_weather_forecast: Get weather forecast for a location using latitude and longitude coordinates

        When users ask about weather:
        1. For weather alerts, ask for the state if not provided, then use get_weather_alerts
        2. For weather forecasts, ask for the location coordinates if not provided, then use get_weather_forecast
        3. Provide clear, helpful responses based on the weather data you retrieve

        If users ask about non-weather topics, politely explain that you are specialized in weather information.

        Always be helpful and provide clear, accurate weather information based on the tools available to you.
        """,
    tools=[mcp_toolset],
)
