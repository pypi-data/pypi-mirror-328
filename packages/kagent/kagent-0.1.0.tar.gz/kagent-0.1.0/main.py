import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import StdioServerParams, mcp_server_tools

from kagent.tools.istio import ProxyConfig

model_client = OpenAIChatCompletionClient(
    model="gpt-4o",
    api_key="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",
)

params = StdioServerParams(
    command="uv",
    args=["run", "kagent", "prometheus", "-u", "http://localhost:9090"],
)

async def main():
  
    tools = await mcp_server_tools(params)
    for tool in tools:
        print(tool.args_type().model_json_schema())
    # print(tools)
    k8s_agent = AssistantAgent(
        "k8s_agent",
        description="An agent for k8s operations",
        tools=tools,
        model_client=model_client,
        system_message="""
      You are a k8s agent. You know how to interact with the Kubernetes API.

      Always prefer wide output format.

      If you don't have any explicit tasks left to complete, return TERMINATE.
      """,
    )


    await Console(k8s_agent.run_stream(task="Perform a query on the prometheus server"))

asyncio.run(main())