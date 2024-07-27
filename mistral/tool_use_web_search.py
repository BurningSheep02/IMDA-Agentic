from autogen import ConversableAgent
import http.client
import json
import os
from web_search import google_search

local_llm_config={
    "config_list": [
        {
            "model": "mistral-nemo:latest", # Loaded with LiteLLM command
            "api_key": "ollama", # Not needed
            "base_url": "http://localhost:11434/v1"  # Your LiteLLM URL
        }
    ],
    "cache_seed": None # Turns off caching, useful for testing different models
}

assistant_agent = ConversableAgent(
    name="Assistant_Agent",
    system_message="You are a helpful AI assistant who obeys the manager. "
    "You can help with google searches by calling google_search"
    "Do not include the function name or result in your response.",
    llm_config=local_llm_config,
)
manager_agent = ConversableAgent(
    name="Manager_Agent",
    system_message="You are a manager.",
    llm_config=local_llm_config,
)

# Register the function with the agent
manager_agent.register_for_llm(name="google_search", description="A web searcher")(google_search)
assistant_agent.register_for_execution(name="google_search")(google_search)

# start the conversation
chat_result = manager_agent.initiate_chat(
    assistant_agent,
    message="Write a profile of Jenny Lee by searching the web for information",
    summary_method="reflection_with_llm",
    max_turns=4,
)