from autogen import ConversableAgent
import http.client
import json
import os


def web_search(query: str) -> str:
    conn = http.client.HTTPSConnection("google.serper.dev")
    payload = json.dumps({
    "q": query
    })
    headers = {
    'X-API-KEY': os.environ.get("SERPER_DEV_API_KEY"),
    'Content-Type': 'application/json'
    }
    conn.request("POST", "/search", payload, headers)
    res = conn.getresponse()
    data = res.read()
    json_data = json.loads(data.decode('utf-8'))
    return json_data



local_llm_config={
    "config_list": [
        {
            "model": "NotRequired", # Loaded with LiteLLM command
            "api_key": "NotRequired", # Not needed
            "base_url": "http://0.0.0.0:4000"  # Your LiteLLM URL
        }
    ],
    "cache_seed": None # Turns off caching, useful for testing different models
}

assistant_agent = ConversableAgent(
    name="Assistant_Agent",
    system_message="You are a helpful AI assistant who obeys the manager. "
    "You can help with google searches by calling web_search and converting the JSON result to human-readable format."
    "Only call this tool once and return 'TERMINATE' when the task is done."
    "Do not include the function name or result in your response.",
    llm_config=local_llm_config,
)
manager_agent = ConversableAgent(
    name="Manager_Agent",
    system_message="You are a manager. ",
    llm_config=local_llm_config,
)

# Register the function with the agent
manager_agent.register_for_llm(name="web_search", description="A google searcher")(web_search)
assistant_agent.register_for_execution(name="web_search")(web_search)

# start the conversation
chat_result = manager_agent.initiate_chat(
    assistant_agent,
    message="Write a profile of Jenny Lee",
    summary_method="reflection_with_llm",
    max_turns=4,
)