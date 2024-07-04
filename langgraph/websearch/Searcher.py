from Agent import Agent
import os

from langchain_core.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools.render import render_text_description
from operator import itemgetter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

import json

class Searcher(Agent):
    @tool
    def web_search(query:str) -> str:
        """Search the web for query"""
        tool = TavilySearchResults(max_results=3,tavily_api_key=os.environ['TAVILY_API_KEY'])
        return tool.invoke(query)

    rendered_tools = render_text_description([web_search])
    prompt = """You are an assistant that has access to the following set of tools. Here are the names and descriptions for each tool: 
    """ + rendered_tools + """
    Given the user input, return the name and input of the tool to use. 
    Return your response as a JSON blob with 'name' and 'arguments' keys.
    For example: 
    {{'name': 'web_search', 'arguments': {{'arg1': "value_1"}}}} """
    
    EXIT_MESSAGE = "No search performed"

    def __init__(self,local_llm='elvee/hermes-2-pro-llama-3:8b-Q5_K_M',temperature=0.0):  
        super().__init__(self, local_llm=local_llm, temperature=temperature)
        self.system_prompt = self.prompt
    
    def search(self,query,ret=""):
        output = super().send(query).replace("\'","\"")
        #print(type(output))
        #print(output)
        try:
            output = json.loads(output)
            print(output["arguments"])
            print(type(output["arguments"]))
            match ret:
                case "url":
                    for x in self.web_search(output["arguments"]):
                        print(x)
                    return [x["url"] for x in self.web_search(output["arguments"])]
                case "":
                    return self.web_search(output["arguments"])
        except Exception as e:
            print(e)
            return self.EXIT_MESSAGE
    

#searcher = Searcher()
#print(searcher.search("Lawrence Wong","url"))




