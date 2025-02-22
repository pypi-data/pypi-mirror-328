"""
Chainlit Integration for Agentic Reasoning System

This module provides a Chainlit-based conversational interface to interact with
the Agentic Reasoning components (Mind Map Agent, Web Search Agent, and Coding Agent).

It serves as the entry point for the Chainlit app.
"""

import chainlit as cl

# Import Agentic Reasoning agents
from agentic_fleet.core.agents.coding_agent import CodingAgent
from agentic_fleet.core.agents.mind_map_agent import MindMapAgent
from agentic_fleet.core.agents.web_search_agent import WebSearchAgent

# Initialize agents (dummy initialization with None)
# In a complete implementation, these would be properly configured with LLMFactory and tools
mind_map_agent = MindMapAgent(llm_factory=None)
web_search_agent = WebSearchAgent(llm_factory=None, web_search_tool=None)
coding_agent = CodingAgent(llm_factory=None, code_execution_tool=None)

@cl.on_message
async def main(message: str):
    """
    Handle incoming Chainlit messages and route them to the appropriate Agentic Reasoning component.

    This is a placeholder function. In a full implementation, the message should be processed
    to decide which agent to activate (e.g., mind map construction, web search, or coding tasks).
    """
    # For demonstration: simply echo the message prefixed with a greeting
    response = f"Agentic Reasoning Response: Received your message -> {message}"
    await cl.Message(content=response).send()

if __name__ == "__main__":
    cl.run()  # Starts the Chainlit server
