from agent.Agent import Agent
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
import re

class SeleniumCrawler(Agent):
    def __init__(self, local_llm='elvee/hermes-2-pro-llama-3:8b-Q5_K_M', temperature=0.0):  
        super().__init__(self, local_llm=local_llm, temperature=temperature)
        try:
            self.driver = webdriver.Safari()
        except:
            self.driver = webdriver.Firefox(service=FirefoxService("/snap/bin/firefox.geckodriver"))

    def _read_webpage(self, url):
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
        except Exception as e:
            print(f"Failed to fetch webpage {url}:\n{e}")
            
        parr = []
        p_elements = self.driver.find_elements(by=By.TAG_NAME, value="p")
        for p_element in p_elements:
            parr.append(p_element.text)
        res = " ".join(parr)
        print(f"-----------\nText extracted from webpage:\n{res}\n-----------\n")
        return res
    
    def _stage(self, context):
        self.system_prompt = """
        You are an expert whose job is to read text extracted from a website, and remove everything irrelevant to the main content.
        You should remove all sources, stylesheets, pictures, and JSON notation, as well as text pertaining to the website's auxiliary functions such as headers, footers, links, navigation menus and terms of use.\n""" 
        if context != "":
            self.system_prompt += f"You should also remove all content irrelevant to {context}."
    
    def crawlSync(self, url, context="") -> str:
        text = self._read_webpage(url)
        self._stage(context)
        try:
            print(f"---- Crawling url {url} synchronously ----\n")
            output = super().sendSync(text)
            print(f"---- Finished crawling url {url} ----\n")
            return output
        except Exception as e:
            print(f"Error occured crawling url {url}\n----\n{e}\n")
            return ""
        
    async def crawl(self, url, context="") -> str:
        text = self._read_webpage(url)
        self._stage(context)
        try:
            print(f"---- Crawling url {url} asynchronously ----\n")
            output = await super().send(text, printout=True)
            print(f"---- Finished crawling url {url} ----\n")
            return output
        except Exception as e:
            print(f"Error occured crawling url {url}\n----\n{e}\n")
            return ""