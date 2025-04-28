from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import MCPToolset


# async def get_tools_async():
#   """Gets tools from the File System MCP Server."""
#   print("Attempting to connect to MCP Filesystem server...")
#   tools, exit_stack = await MCPToolset.from_server(
#       # Use StdioServerParameters for local process communication
#       connection_params=StdioServerParameters(
#           command='npx', # Command to run the server
#           args=["-y",    # Arguments for the command
#                 "@modelcontextprotocol/server-filesystem",
#                 # TODO: IMPORTANT! Change the path below to an ABSOLUTE path on your system.
#                 "/path/to/your/folder/"],
#       )
#       # For remote servers, you would use SseServerParams instead:
#       # connection_params=SseServerParams(url="http://remote-server:port/path", headers={...})
#   )
#   print("MCP Toolset created successfully.")
#   # MCP requires maintaining a connection to the local MCP Server.
#   # exit_stack manages the cleanup of this connection.
#   return tools, exit_stack
from google.adk.tools.mcp_tool.mcp_session_manager import SseServerParams


async def get_tools_async():
    tools, exit_stack = await MCPToolset.from_server(
        connection_params=SseServerParams(
            # url="https://mcp-hello-world-393833795300.us-central1.run.app/sse"
            url="http://localhost:8000/sse"
        )
    )
    # Keep exit_stack open for the lifetime of the container.
    return tools, exit_stack

async def create_agent():
  """Gets tools from MCP Server."""
  tools, exit_stack = await get_tools_async()

  agent = LlmAgent(
      model='gemini-2.0-flash', # Adjust model name if needed based on availability
      name='filesystem_assistant',
      instruction='Help user interact with the local filesystem using available tools.',
      tools=tools, # Provide the MCP tools to the ADK agent
  )
  return agent, exit_stack


root_agent = create_agent()