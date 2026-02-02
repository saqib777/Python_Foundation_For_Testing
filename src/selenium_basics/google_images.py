from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.google.com")

    wait = WebDriverWait(driver, 10)

    # Click on the "Images" link
    images_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Images"))
    )
    images_link.click()

    # Wait for the Images search box and search
    search_box = wait.until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Selenium WebDriver")
    search_box.submit()

    # Wait for image results and click the first image
    first_image = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "img.Q4LuWd")
        )
    )
    first_image.click()

    driver.quit()


if __name__ == "__main__":
    main()
