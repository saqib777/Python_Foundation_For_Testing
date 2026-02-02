# src/pages/google_home_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
   

    SEARCH_BOX = (By.NAME, "q")
    IMAGES_LINK = (By.LINK_TEXT, "Images")
    FIRST_IMAGE = (By.CSS_SELECTOR, "img.rg_i") #This was changed from FIRST_IMAGE = (By.CSS_SELECTOR, "img.Q4LuWd")


    def open(self):
     self.driver.get("https://www.google.com")
     self.accept_consent_if_present()

    def go_to_images(self):
        self.wait.until(EC.element_to_be_clickable(self.IMAGES_LINK)).click()

    def search(self, text):
        box = self.wait.until(EC.presence_of_element_located(self.SEARCH_BOX))
        box.send_keys(text)
        box.submit()

    def click_first_image(self):
     images = self.wait.until(
        EC.presence_of_all_elements_located(self.FIRST_IMAGE)
    )

     first_image = images[0]
     self.driver.execute_script("arguments[0].scrollIntoView(true);", first_image)
     self.wait.until(EC.element_to_be_clickable(first_image))
     first_image.click()

    def is_image_preview_open(self):
     preview = self.wait.until(
         EC.presence_of_element_located((By.ID, "Sva75c"))
     )
     return preview.is_displayed()

    def accept_consent_if_present(self):
     try:
         agree_button = WebDriverWait(self.driver, 5).until(
             EC.element_to_be_clickable((By.XPATH, "//button//*[text()='Accept all']"))
         )
         agree_button.click()
     except:
        pass
