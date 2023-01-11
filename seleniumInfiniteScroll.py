# Test: Scraping E-Commerce test site with infinite scroll
# URL: https://webscraper.io/test-sites/e-commerce/scroll/computers/laptops
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import re
from selenium.common.exceptions import NoSuchElementException

driver = Service("chromedriver")
page = webdriver.Chrome(service=driver)
page.get("https://webscraper.io/test-sites/e-commerce/scroll/computers/laptops")
# Explicit wait for 2 seconds
time.sleep(2)

# Get height of current screen
screen_height = page.execute_script("return window.screen.height")
i = 1

while True:
    page.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(1)
    # Below variable represents screen height.  Will compare to screen height * i to kmnow when to exit loop
    scroll_height = page.execute_script("return document.body.scrollHeight;")
    if (screen_height) * i > scroll_height:
        break
print("Scroll complete!")