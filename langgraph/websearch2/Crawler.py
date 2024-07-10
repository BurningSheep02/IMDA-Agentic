from Agent import Agent
from urllib.request import urlopen,Request
import pythonmonkey as pm
from pythonmonkey import require as js_require
import re

def open_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    req = Request(url, headers=headers) 
    html = urlopen(req).read()
    return html

js_lib = js_require('./turndown.js')
def parse_html(html):
    md = js_lib.html_to_markdown(html)
    md = md.replace(r"\\n", "").replace(r"\\t","")
    md = re.sub(r'\n+', '\n', md)
    return md

class Crawler(Agent):
    def __init__(self,local_llm='elvee/hermes-2-pro-llama-3:8b-Q5_K_M',temperature=0.0):  
        super().__init__(self, local_llm=local_llm, temperature=temperature)

    def crawl(self,url,context="") -> str:
        try:
            html = str(open_url(url))
            print(f"----\nOpening {url}\n")
        except Exception as e:
            print(f"Failed to open url {url} for the following reason:\n{e}")
            return ""
        
        self.system_prompt = """
        You are an expert whose job is to parse text files extracted from a website.
        Ignore all sources, style tags, pictures, and JSON notation. Return only on the relevant content""" 

        if context != "":
            self.system_prompt += "about" + context
        try:
            output = super().send(parse_html(html))
            print(f"Finished crawling url {url}\n----")
            return output
        except Exception as e:
            print(f"Error occured crawling url {url}\n----")
            print(e)
            return ""

#crawler = Crawler()
#print(crawler.crawl(url="https://www.bbc.com/news/world-asia-32604122", context="Amos Yee"))