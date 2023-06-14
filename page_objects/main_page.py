import allure
from locators.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Принять cookies')
    def accept_cookies(self):
        self.find_element_located(MainPageLocators.COOKIE_ACCEPT_BUTTON_LOCATOR).click()

    @allure.step('Пролистать до раздела "Вопросы о важном" на главной странице')
    def scroll_to_the_most_asked_questions_section(self):
        section = self.find_element_located(MainPageLocators.MOST_ASKED_QUESTIONS_SECTION_HEADING_LOCATOR)
        self.scroll_to_element(section)
        self.wait_element_visible(MainPageLocators.QUESTION_LOCATOR)

    @allure.step('Нажать на каждый вопрос')
    def click_on_questions(self, index):
        self.wait_element_visible(MainPageLocators.QUESTION_LOCATOR)
        questions = self.find_elements_located(MainPageLocators.QUESTION_LOCATOR)
        questions[index].click()

    @allure.step('Получить текст ответа на вопрос')
    def get_answers(self):
        self.wait_element_visible(MainPageLocators.ANSWER_LOCATOR)
        return self.find_element_located(MainPageLocators.ANSWER_LOCATOR).text

    @allure.step('Нажать на кнопку "Заказать" в правом верхнем углу главной страницы')
    def click_on_top_order_button(self):
        self.find_element_located(MainPageLocators.TOP_ORDER_BUTTON_LOCATOR).click()

    @allure.step('Пролистать до кнопки "Заказать" в нижней части главной страницы')
    def scroll_to_the_bottom_order_button(self):
        button = self.find_element_located(MainPageLocators.BOTTOM_ORDER_BUTTON_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)

    @allure.step('Нажать на кнопку "Заказать" в нижней части главной страницы')
    def click_on_bottom_order_button(self):
        self.find_element_located(MainPageLocators.BOTTOM_ORDER_BUTTON_LOCATOR).click()

    @allure.step('Ожидание загрузки логотипа Дзен')
    def wait_for_dzen_logo(self):
        self.wait_element_visible(MainPageLocators.DZEN_LOGO_LOCATOR)
