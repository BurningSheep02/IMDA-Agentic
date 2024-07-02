import os

from autogen import ConversableAgent

config_list = [
    {
        "model": "llama3",
        "base_url": "http://localhost:11434/v1", # Default for ollama
        "api_key": "ollama",
    }
]
    
agent = ConversableAgent(
    "chatbot",
    llm_config={"config_list": config_list},
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
)

reply = agent.generate_reply(messages=[{"content": "Tell me about yourself"
                , "role": "user"}])
print(reply)