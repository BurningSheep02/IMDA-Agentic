from firecrawl import FirecrawlApp
import os

app = FirecrawlApp(api_key=os.environ['FIRECRAWL_APP_API_KEY'])

content = app.scrape_url("")
print(content)

