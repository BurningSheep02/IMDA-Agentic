from Crawler import Crawler
from SeleniumCrawler import SeleniumCrawler
from ChromaClient import ChromaClient
from Searcher import search
from Summariser import Summariser
import asyncio

# https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#response

async def main():

    # crawler = Crawler()
    crawler = SeleniumCrawler()
    summariser = Summariser()
    chroma = ChromaClient()
    TARGET_PERSON = "Zara Khanna"

    urls = search(TARGET_PERSON)
    res = []
    for url in urls:
        res.append(await crawler.crawl(url,context=TARGET_PERSON))
    res += chroma.similarity_search(TARGET_PERSON, k=3)
    summary = await summariser.summarise(res,TARGET_PERSON)

    print("""\n\nResult:\n\n""")
    print(summary)

if __name__ == "__main__":
    asyncio.run(main())