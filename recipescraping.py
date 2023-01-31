from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from selenium.common.exceptions import NoSuchElementException

driver = Service("chromedriver")
scraper = webdriver.Chrome(service=driver)
search_query = "breakfast"
scraper.get(f"https://theproteinchef.co/recipes/?fwp_search={search_query}")
data = []
count = 1

while True:
    time.sleep(2)
    recipes = scraper.find_elements(By.CLASS_NAME,'fl-post-column')
    print(f"Page {count} scraping...!")
    for recipe in recipes:
        img = recipe.find_element(By.TAG_NAME,"img").get_attribute("src")
        name = recipe.text
        href = recipe.find_element(By.TAG_NAME,"a").get_attribute("href")
        data.append({"img":img,"name":name,"href":href,"type":search_query})
    print(f"Page {count} complete!")
    count += 1

    try:
        next_button = WebDriverWait(scraper,10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='next page-numbers']")))
        next_button.click()
    except NoSuchElementException:
        break
for recipe in data:
    print(recipe)
print("Scroll complete!")