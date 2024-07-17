from Crawler import Crawler
from SeleniumCrawler import SeleniumCrawler
from ChromaClient import ChromaClient
from Searcher import search
from Summariser import Summariser
from GuardianNewsAgent import GuardianNewsAgent
import asyncio

# https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#response

async def main():

    # crawler = Crawler()
    crawler = SeleniumCrawler()
    summariser = Summariser()
    newser = GuardianNewsAgent()
    #chroma = ChromaClient()
    TARGET_PERSON = "Donald Trump"

    urls = search(TARGET_PERSON,urls=1)
    res = []
    for url in urls:
        res.append(await crawler.crawl(url,context=TARGET_PERSON))
    res += newser.guardian_search(TARGET_PERSON) 
    
    #res += chroma.similarity_search(TARGET_PERSON, k=3)
    summary = await summariser.summarise(res,TARGET_PERSON)

    print("""\n\nResult:\n\n""")
    print(summary)

if __name__ == "__main__":
    asyncio.run(main())