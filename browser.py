import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def get_site(url: str):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    time.sleep(2)
    return driver.page_source
