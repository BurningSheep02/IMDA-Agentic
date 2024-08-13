from click import wrap_text
from typing_extensions import Annotated

from autogen import (
    Agent,
    AssistantAgent,
    GroupChat,
    GroupChatManager,
    UserProxyAgent,
    config_list_from_json,
    register_function,
)

from autogen.cache import Cache


from web_search import search_and_crawl


name = "Lee Hsien Loong"
task = (
    f"Write a profile of {name}. Include sections on education, career, and recent achievements. "
)


config_list = [
        {
            "model": "mistral-nemo:latest", # Loaded with LiteLLM command
            "api_key": "ollama", # Not needed
            "base_url": "http://localhost:11434/v1"  # Your LiteLLM URL
            
        }
    ]

user_proxy = UserProxyAgent(
    name="Admin",
    system_message="A human admin. Give the task, and send instructions to writer to refine the profile.",
    code_execution_config=False,
)

planner = AssistantAgent(
    name="Planner",
    system_message="""Planner. Given a task, please determine what information is needed to complete the task. """,
    llm_config={"config_list": config_list, "cache_seed": None},
)

crawler = AssistantAgent(
    name="Crawler",
    llm_config={"config_list": config_list, "cache_seed": None},
    system_message="""Crawler. Your job is to craft a query to search for relevant information based on the information required by the planner.
""",
)

crawler.register_for_llm(name="search_and_crawl", description="A web searcher")(search_and_crawl)
user_proxy.register_for_execution(name="search_and_crawl")(search_and_crawl)

writer = AssistantAgent(
    name="Writer",
    llm_config={"config_list": config_list, "cache_seed": None},
    system_message="""Writer. Please write the profile in markdown format (with relevant titles) and put the content in pseudo ```md``` code block, based on the planner's instructions.
    You will write it for a task based on previous chat history. 
    Extract relevant information from the result of the crawler's tool call.""",
)

def custom_speaker_selection_func(last_speaker: Agent, groupchat: GroupChat):
    """Define a customized speaker selection function.
    A recommended way is to define a transition for each speaker in the groupchat.

    Returns:
        Return an `Agent` class or a string from ['auto', 'manual', 'random', 'round_robin'] to select a default method to use.
    """
    messages = groupchat.messages

    if len(messages) <= 1:
        # first, let the planner delegate the tasks
        return planner

    if last_speaker is planner:
        # if the last message is from planner, let the crawler search
        return crawler
    
    elif last_speaker is user_proxy:
        if messages[-1]["content"].strip() != "" and messages[-1]["content"].strip()[0] == "#" :
            # If the last message is from user and is not empty, let the writer continue
            return writer
        else: 
            return planner     

    elif last_speaker is crawler:
        return user_proxy

    elif last_speaker is writer:
        # Always let the user to speak after the writer
        return user_proxy

    else:
        # default to auto speaker selection method
        return "auto"


groupchat = GroupChat(
    agents=[user_proxy, writer, crawler, planner],
    messages=[],
    max_round=10,
    speaker_selection_method=custom_speaker_selection_func,
)
manager = GroupChatManager(groupchat=groupchat, llm_config={"config_list": config_list, "cache_seed": None})

with Cache.disk(cache_seed=41) as cache:
    groupchat_history_custom = user_proxy.initiate_chat(
        manager,
        message=task,
        #cache=cache,
    )