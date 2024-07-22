# import http.client
# import json
# import os

# def search(query,urls=3):
#     """
#     returns a list of urls produced by serper.dev on google search
#     """
#     conn = http.client.HTTPSConnection("google.serper.dev")
#     payload = json.dumps({
#         "q": query,
#         "gl": "sg"
#     })
#     headers = {
#     'X-API-KEY': os.environ['SERPER_DEV_API_KEY'],
#     'Content-Type': 'application/json'
#     }
#     conn.request("POST", "/search", payload, headers)
#     res = conn.getresponse()
#     data = res.read()
#     data = json.loads(data.decode("utf-8"))
    
#     return [res["link"] for res in data["organic"][0:urls]]


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search(query,urls=3,blacklist=['google','youtu'],prunelist=['wikipedia']):
    
    url = "https://www.google.com"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)

    search_box = driver.find_element(By.ID, "APjFqb")
    search_box.click()
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)

    try:
        elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "gsr")) #This is a dummy element
    )
    except:
        print("No search results")
    
    def not_blacklisted(link):
        is_not_in_blacklist = [word not in link for word in blacklist]
        return all(is_not_in_blacklist)
    links = list(map(lambda x : x.get_attribute("href"),driver.find_elements(By.XPATH, "//a[@href]")))

    links = list(dict.fromkeys(filter(not_blacklisted,links)))

    

    driver.quit()

    return links[0:urls]





