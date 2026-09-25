
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CandyStar:

    URL = "https://candystar.ro/"

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.bomboane = (By.CSS_SELECTOR, "a[href='https://candystar.ro/categorie-produs/bomboane/']")
        self.sour_candy = (By.CSS_SELECTOR, "a[href='https://candystar.ro/categorie-produs/sour-candy/']")
        self.jeleuri = (By.CSS_SELECTOR, "a[href='https://candystar.ro/categorie-produs/jeleuri/']")

    def open(self):
        self.driver.get(self.URL)

    def click_bomboane(self):
        self.wait.until(EC.element_to_be_clickable(self.bomboane)).click()

    def click_sour_candy(self):
        self.wait.until(EC.element_to_be_clickable(self.sour_candy)).click()

    def click_jeleuri(self):
        self.wait.until(EC.element_to_be_clickable(self.jeleuri)).click()

    def get_title(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))).text
    

