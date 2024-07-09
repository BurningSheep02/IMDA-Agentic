#from Naked.toolshed.shell import run_js
import pythonmonkey as pm
from pythonmonkey import require as js_require
import re

js_lib = js_require('./turndown.js')

from urllib.request import urlopen, Request

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
#reg_url = "https:XXXXOOOO"
req = Request("", headers=headers) 
html = str(urlopen(req).read())
md = js_lib.html_to_markdown(html)
md = md.replace(r"\\n", "").replace(r"\\t","")
md = re.sub(r'\n+', '\n', md)

print(md)