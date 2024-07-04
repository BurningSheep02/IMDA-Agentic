from Agent import Agent
from urllib.request import urlopen,Request

def open_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    req = Request(url, headers=headers) 
    html = urlopen(req).read()
    return html

class Crawler(Agent):
    def __init__(self,local_llm='elvee/hermes-2-pro-llama-3:8b-Q5_K_M',temperature=0.0):  
        super().__init__(self, local_llm=local_llm, temperature=temperature)

    def crawl(self,url) -> str:
        try:
            html = open_url(url)
        except Exception as e:
            print(f"Failed to open url {url} for the following reason:\n{e}")
            return ""
        
        self.system_prompt = str(html).replace("{", "[").replace("}", "]")+ """
        You are an expert whose job is to parse html files and return what a human would like to read.
        Extract the text from the preceding html file. Remove all style, code and media tags. 
        Remove all sources and references, focusing only on the salient content.""" 
        try:
            output = super().send()
            print(f"Finished crawling url {url}\n\n")
            return output
        except Exception as e:
            print(f"Error occured crawling url {url}\n\n")
            print(e)
            return ""


    #crawler = Crawler()
    #rint(crawler.crawl("https://www.britannica.com/biography/Lawrence-Wong"))