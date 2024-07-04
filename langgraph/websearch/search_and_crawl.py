from Crawler import Crawler
from Searcher import Searcher
from Summariser import Summariser

crawler = Crawler()
searcher = Searcher()
summariser = Summariser()
TARGET_PERSON = "Lawrence Wong"

urls = searcher.search(TARGET_PERSON,"url")
res = []
for url in urls:
    res.append(crawler.crawl(url))
summary = summariser.summarise(res,TARGET_PERSON)
print("""\n\nResult:\n\n""")
print(summary)