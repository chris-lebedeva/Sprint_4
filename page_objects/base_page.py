from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data.urls import Urls


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = Urls.SCOOTER_MAIN_PAGE_URL

    def click(self, element):
        element.click()

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Элемент {locator} не найден")

    def find_elements_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Элементы {locator} не найдены")
