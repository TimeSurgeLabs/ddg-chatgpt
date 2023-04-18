import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

def get_site(url: str):
    driver.get(url)
    time.sleep(2)
    return driver.page_source
