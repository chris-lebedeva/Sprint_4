from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage


# Класс с методами главной страницы
class MainPageHelper(BasePage):
    def accept_cookies(self):
        self.find_element_located(MainPageLocators.COOKIE_ACCEPT_BUTTON_LOCATOR).click()

    def scroll_to_the_most_asked_questions_section(self):
        section = self.find_element_located(MainPageLocators.MOST_ASKED_QUESTIONS_SECTION_HEADING_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView();", section)

    def click_on_questions_get_answers(self, driver):
        questions = self.find_elements_located(MainPageLocators.QUESTION_LOCATOR)
        answers = []
        for question in questions:
            question.click()
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.ANSWER_LOCATOR))
            answer = self.find_element_located(MainPageLocators.ANSWER_LOCATOR).text
            answers.append(answer)
        return answers

    def click_on_top_order_button(self):
        self.find_element_located(MainPageLocators.TOP_ORDER_BUTTON_LOCATOR).click()

    def scroll_to_the_bottom_order_button(self):
        button = self.find_element_located(MainPageLocators.BOTTOM_ORDER_BUTTON_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)

    def click_on_bottom_order_button(self):
        self.find_element_located(MainPageLocators.BOTTOM_ORDER_BUTTON_LOCATOR).click()

    def current_url(self):
        return self.driver.current_url

    def wait_for_dzen_logo(self, driver):
        self.find_element_located(MainPageLocators.DZEN_LOGO_LOCATOR)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.DZEN_LOGO_LOCATOR))
