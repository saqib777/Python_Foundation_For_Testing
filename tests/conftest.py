import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()

# Headless mode (disabled for now so we can visually see the browser during learning/debugging)
# if os.getenv("HEADLESS") == "true":
#     options.add_argument("--headless=new")
#     options.add_argument("--window-size=1920,1080")


    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
