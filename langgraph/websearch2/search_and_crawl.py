from Crawler import Crawler
from SeleniumCrawler import SeleniumCrawler
from Searcher import search
from Summariser import Summariser
import asyncio

async def main():

    crawler = Crawler()
    crawler2 = SeleniumCrawler()
    summariser = Summariser()
    TARGET_PERSON = "Mao Zedong"

    urls = search(TARGET_PERSON)
    res = []
    for url in urls:
        res.append(await crawler2.crawl(url,context=TARGET_PERSON))
    summary = await summariser.summarise(res,TARGET_PERSON)

    print("""\n\nResult:\n\n""")
    print(summary)

if __name__ == "__main__":
    asyncio.run(main())