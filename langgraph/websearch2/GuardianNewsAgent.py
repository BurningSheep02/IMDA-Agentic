from aiohttp import Payload
from Agent import Agent
import requests
import json

class GuardianNewsAgent(Agent):
    def __init__(self,local_llm='elvee/hermes-2-pro-llama-3:8b-Q5_K_M',temperature=0.0):  
        super().__init__(self, local_llm=local_llm, temperature=temperature)
    
    def guardian_search(self, query, N=3):
        url = 'https://content.guardianapis.com/search'
        params = {'api-key':'80f116f3-eecb-4c7c-b52f-f4b211ca26b9',
                'format': "json",
                'q': query,
                'show-fields': ['body'],
                }

                
        res = requests.get(url, params=params).text
        res = json.loads(res)
        articles = res['response']['results'][0:N]
        
        
        print("---- Articles found ----\n")
        for article in articles:
            print("Article headlines: " + article['webTitle'] + "\n")
            #print("Article text: " + article['fields']['body'] + "\n")
        
        texts = [article['fields']['body'] for article in articles]
        return texts
    

    
myAgent = GuardianNewsAgent()
myAgent.guardian_search("Donald Trump")