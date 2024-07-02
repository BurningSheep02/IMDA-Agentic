import autogen

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


llm_config = {
    "config_list":  [
        {
            "model": "NotRequired", # Loaded with LiteLLM command
            "api_key": "NotRequired", # Not needed
            "base_url": "http://0.0.0.0:4000"  # Your LiteLLM URL
        }
    ],
    "cache_seed": None,
    "functions":[
        {
            "name": "web_search",
            "description": "returns a json object containing the results of your query",
            "parameters": {
                "type": "object",
                "properties": {
                    "query":{
                        "type": "string",
                        "description": "The query to be researched"
                    }
                },
                "required": ["query"]
            }
        },
    ]
}


# Create the agent and include examples of the function calling JSON in the prompt
# to help guide the model
assistant = autogen.AssistantAgent(
    name="assistant",
    system_message="You are a helpful AI assistant. "
    "You can help with google searches by calling web_search"
    "Summarise the JSON results to human-readable text "
    "return 'TERMINATE' when the task is done."
    "Do not include the function name or result in your response.",

    llm_config=llm_config,
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    is_termination_msg=lambda x: x.get("content", "") and "TERMINATE" in x.get("content", ""),
    human_input_mode="NEVER",
    max_consecutive_auto_reply=2,
)

# Register the function with the agent
assistant.register_for_llm(name="web_search", description="A google searcher")(web_search)
user_proxy.register_for_execution(name="web_search")(web_search)

# start the conversation
res = user_proxy.initiate_chat(
    assistant,
    message="Write a short profile of Jenny Lee",
    summary_method="reflection_with_llm",
)