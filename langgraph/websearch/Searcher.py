import os
from langchain_community.chat_models import ChatOllama
from langgraph.graph.message import add_messages

local_llm = 'elvee/hermes-2-pro-llama-3:8b-Q5_K_M'
llm = ChatOllama(model=local_llm, temperature=0)

from langchain_core.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools.render import render_text_description

from operator import itemgetter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

@tool
def web_search(query:str) -> str:
    """Search the web for query"""
    tool = TavilySearchResults(max_results=3,tavily_api_key=os.environ['TAVILY_API_KEY'])
    return str(tool.invoke(query))

class Searcher():
    def __init__(self,local_llm='elvee/hermes-2-pro-llama-3:8b-Q5_K_M',max_results=3):  
        self.llm = ChatOllama(model=local_llm, temperature=0)

    def search(self,user_input):
        rendered_tools = render_text_description([web_search])
        
        system_prompt = """You are an assistant that has access to the following set of tools. Here are the names and descriptions for each tool: 
        """ + rendered_tools + """
        Given the user input, return the name and input of the tool to use. 
        Return your response as a JSON blob with 'name' and 'arguments' keys.
        For example: 
        {{'name': 'web_search', 'arguments': {{'arg1': "value_1"}}}} """

        prompt = ChatPromptTemplate.from_messages(
        [("system", system_prompt), ("user", "{input}")]
        )

        query_chain = prompt | self.llm | JsonOutputParser() | itemgetter("arguments") 
        
        query = query_chain.invoke({"input": user_input})
        print(f"I'm searching for {query}")
        return web_search(query)
    
searcher = Searcher()
print(searcher.search("Lawrence Wong"))




