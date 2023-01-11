# Test URL https://pokeratlas.com/poker-tournaments/appalachia/upcoming

'''
Flow of URLS:
Start on https://pokeratlas.com/areas
Break into sections for each state
Select the link under each state
Select "See All Tournaments"
Endless Scroll scrape --> You Are Here!!
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException

driver = Service("chromedriver")
page = webdriver.Chrome(service=driver)
page.get("https://pokeratlas.com/poker-tournaments/appalachia/upcoming")
# Explicit wait for popup to load
# Button class = "modal-close" --> click
try:
    ad_button = WebDriverWait(page, 3).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'modal-close')))
    ad_button.click()
except TimeoutException:
    print("No ad window found")

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