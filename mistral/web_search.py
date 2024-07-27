from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from typing_extensions import Annotated

def not_blacklisted(blacklist):
    def link_not_blacklisted(link):
        is_not_in_blacklist = [word not in link for word in blacklist]
        return all(is_not_in_blacklist)
    return link_not_blacklisted

def google_search(
    query: Annotated[str, 'query to search for'],
    blacklist=['google','youtu'], 
    n=5):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.google.com/search?q="+query)

    links = list(map(lambda x : x.get_attribute("href"), driver.find_elements(By.XPATH, "//a[@href]"))) 
    links = list(dict.fromkeys(filter(not_blacklisted(blacklist),links)))
    
    return links[0:n]

