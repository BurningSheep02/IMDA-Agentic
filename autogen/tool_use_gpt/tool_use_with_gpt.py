from autogen import ConversableAgent, UserProxyAgent
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
    "config_list": [
        {
            "model": "phi3", 
            "base_url": "http://localhost:1234/v1", 
            "api_key": "lm-studio"
        }
    ]
}

# Let's first define the assistant agent that suggests tool calls.
assistant = ConversableAgent(
    name="Assistant",
    system_message="You are a helpful AI assistant. "
    "You can help with google searches by calling web_search and converting the JSON result to human-readable format."
    "Return 'TERMINATE' when the task is done.",
    llm_config=llm_config,

)

user_proxy = UserProxyAgent(
    name="User",
    llm_config=False,
    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    code_execution_config=False
)

#Register the tool signature with the assistant agent.
assistant.register_for_llm(name="web_search", description="A Google searcher")(web_search)
user_proxy.register_for_execution(name="web_search")(web_search)

chat_result = user_proxy.initiate_chat(assistant, message="Write a profile of Lawrence Wong.")
