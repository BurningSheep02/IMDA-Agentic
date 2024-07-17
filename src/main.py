from agent.SeleniumCrawler import SeleniumCrawler
from agent.Summariser import Summariser
from chroma.ChromaDatabase import ChromaDatabase
from chroma.ChromaTemp import ChromaTemp

from Searcher import search

import asyncio

async def main():

    crawler = SeleniumCrawler()
    summariser = Summariser()
    # QUERY = "Write a summary of the target."
    QUERY_TARGET = "Zara Khanna"

    # External search online
    urls = search(QUERY_TARGET)
    webpages = []
    for url in urls:
        webpages.append(await crawler.crawl(url, context=QUERY_TARGET))
    web_res = ChromaTemp(webpages, QUERY_TARGET, k=20)

    # Internal search in database
    chroma_db = ChromaDatabase()
    db_res = chroma_db.similarity_search(QUERY_TARGET, k=3)

    # Put everything together and summarise
    res = web_res + db_res
    summary = await summariser.summarise(res, QUERY_TARGET)

    print("""\n\nResult:\n\n""")
    print(summary)

if __name__ == "__main__":
    asyncio.run(main())