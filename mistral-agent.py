from smolagents.agents import ToolCallingAgent
from smolagents import tool, LiteLLMModel
from typing import Optional

model = LiteLLMModel(
    model_id="ollama_chat/mistral",
    api_base="http://localhost:11434",
    api_key=None 
)


@tool
def addition(num1: str, num2: str) -> int:
    """
    Adds two numbers together.

    Args:
        num1: first number
        num2: second number
    """
    answer = int(num1) + int(num2)

    return f"The result of adding {num1} + {num2} is {answer}"


@tool
def subtraction(num1: str, num2: str) -> int:
    """
    Subtracts the second number from the first.

    Args:
        num1: first number
        num2: second number

    Returns:
        The difference as an integer.
    """
    return int(num1) - int(num2)

@tool
def multiplication(num1: str, num2: str) -> int:
    """
    Multiplies two numbers.

    Args:
        num1: first number
        num2: second number

    Returns:
        The product as an integer.
    """
    return int(num1) * int(num2)



agent = ToolCallingAgent(tools=[addition], model=model)

print(agent.run("What's 1 plus 1?"))