from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.models.lite_llm import LiteLlm
import os

MODEL = "gemma3:4b"

root_agent = Agent(
    name="search_assistant",
    model=LiteLlm(model=f"ollama/{MODEL}"),
    instruction="You are a helpfull assistant. You always answer the questions only if you definately know the answer.",
    description="A helpful assistant that browses the web for information.",
    tools=[]
)