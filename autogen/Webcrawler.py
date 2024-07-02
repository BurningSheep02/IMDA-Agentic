
import http.client
import json
import os

def web_search(query: str) -> str:
    conn = http.client.HTTPSConnection("google.serper.dev")
    payload = json.dumps({
    "q": query
    })
    headers = {
    'X-API-KEY': os.environ.get("SERPER_DEV_API_KEY"),
    'Content-Type': 'application/json'
    }
    conn.request("POST", "/search", payload, headers)
    res = conn.getresponse()
    data = res.read()
    json_data = json.loads(data.decode('utf-8'))
    return json_data

print(web_search("Lawrence Wong"))
