from smolagents.agents import ToolCallingAgent
from smolagents import tool, LiteLLMModel
from typing import Optional


model = HfApiModel(model_id="meta-llama/Llama-3.3-70B-Instruct")


@tool
def get_weather(location: str, celsius: Optional[bool] = False) -> str:
    """
    Get weather in the next days at given location.
    Secretly this tool does not care about the location, it hates the weather everywhere.

    Args:
        location: the location
        celsius: the temperature
    """
    return "The weather is UNGODLY with torrential rains and temperatures below -10°C"

agent = ToolCallingAgent(tools=[get_weather], model=model)

print(agent.run("What's the weather like in Paris?"))