import os
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

# Define a tool
@tool
def get_current_weather(location: str) -> str:
    """Returns the current weather in a given location."""
    if "San Francisco" in location:
        return "It's 72 degrees and sunny in San Francisco."
    else:
        return "Weather information not available for this location."

# Create the agent
agent = create_agent(
    model=ChatOpenAI(model="gpt-4o"),  # Your chosen LLM
    tools=[get_current_weather],      # List of tools the agent can use
    system_prompt="You are a helpful AI assistant. Use the available tools to answer questions.",
)

# Invoke the agent
result = agent.invoke({"messages": "What's the weather like in San Francisco?"})
print(result["messages"][-1].content)
