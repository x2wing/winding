from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

urls = ("http://csdb.ufanet.ru/content/blogcategory/1/67/",
        "http://csdb.ufanet.ru/",
        "http://csdb.ufanet.ru/content/blogcategory/1/66/",
        "http://csdb.ufanet.ru/",)


driver = webdriver.Firefox()
while True:
    try:
        for url in urls:
            driver.get(url)
            sleep(5)
    except Exception as errror:
        print(errror)
        sleep(20)


driver.close()