import time

import httpx
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def get_site(url: str):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    time.sleep(2)
    return driver.page_source


def get_raw(url: str):
    resp = httpx.get(url, follow_redirects=True)
    return resp.text


if __name__ == "__main__":
    print(get_raw("https://github.com/ava-labs/subnet-evm/raw/master/contracts/contracts/AllowList.sol"))
