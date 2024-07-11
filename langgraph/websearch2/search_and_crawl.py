from Crawler import Crawler
from Searcher import search
from Summariser import Summariser

crawler = Crawler()
summariser = Summariser()
TARGET_PERSON = "Mao Zedong"

urls = search(TARGET_PERSON)
res = []
for url in urls:
    res.append(crawler.crawl(url,context=TARGET_PERSON))
summary = summariser.summarise(res,TARGET_PERSON)

print("""\n\nResult:\n\n""")
print(summary)