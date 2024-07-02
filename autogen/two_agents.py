import os

from autogen import ConversableAgent

config_list = [
    {
        "model": "llama3",
        "base_url": "http://localhost:11434/v1", # Default for ollama
        "api_key": "ollama",
    }
]

student_agent = ConversableAgent(
    name="Student_Agent",
    system_message="You are a student willing to learn.",
    llm_config={"config_list": config_list},
)
teacher_agent = ConversableAgent(
    name="Teacher_Agent",
    system_message="You are a math teacher.",
    llm_config={"config_list": config_list},
)

chat_result = student_agent.initiate_chat(
    teacher_agent,
    message="What is the orbit-stabiliser theorem?",
    summary_method="reflection_with_llm",
    max_turns=2,
)