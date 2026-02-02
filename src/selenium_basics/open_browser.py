from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.google.com")

    wait = WebDriverWait(driver, 10)
    search_box = wait.until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # search_box.send_keys("Selenium WebDriver")
    # search_box.submit()

    driver.quit()


if __name__ == "__main__":
    main()
