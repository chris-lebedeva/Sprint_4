import allure
from enum import Enum
from locators.order_page_locators import OrderPageLocators
from page_objects.base_page import BasePage


class OrderPage(BasePage):
    class RentalPeriod(Enum):
        ONE_DAY = 'сутки'
        TWO_DAYS = 'двое суток'

    class Color(Enum):
        BLACK = 'чёрный жемчуг'
        GREY = "серая безысходность"

    @allure.step('Заполнить информацию о клиенте на странице оформления заказа: '
                 'имя, фамилия, адрес, станция метро, номер телефона, дата аренды')
    def fill_in_client_info(self, first_name, last_name, street_address, phone_number):
        self.find_element_located(OrderPageLocators.FIRST_NAME_LOCATOR).send_keys(first_name)
        self.find_element_located(OrderPageLocators.LAST_NAME_LOCATOR).send_keys(last_name)
        self.find_element_located(OrderPageLocators.STREET_ADDRESS_LOCATOR).send_keys(street_address)
        self.find_element_located(OrderPageLocators.STATION_LOCATOR).click()
        station = self.find_element_located(OrderPageLocators.REQUIRED_STATION_LOCATOR)
        self.scroll_to_element(station)
        station.click()
        self.find_element_located(OrderPageLocators.PHONE_NUMBER_LOCATOR).send_keys(phone_number)
        self.find_element_located(OrderPageLocators.NEXT_BUTTON).click()
        self.find_element_located(OrderPageLocators.RENTAL_DATE_LOCATOR).click()
        next_day = self.find_element_located(OrderPageLocators.NEXT_DAY_LOCATOR)
        excluded_day = self.find_element_located(OrderPageLocators.EXCLUDED_DATE_LOCATOR)
        if next_day == excluded_day:
            self.find_element_located(OrderPageLocators.REPLACED_DATE_LOCATOR).click()
        else:
            next_day.click()

    @allure.step('Заполнить информацию о заказе:'
                 'срок аренды, цвет самоката, комментарий')
    def fill_in_order_details(self, rental_period, color, comment):
        rental_period_locators = {
            OrderPage.RentalPeriod.ONE_DAY: OrderPageLocators.ONE_DAY_LOCATOR,
            OrderPage.RentalPeriod.TWO_DAYS: OrderPageLocators.TWO_DAYS_LOCATOR
        }
        color_locators = {
            OrderPage.Color.BLACK: OrderPageLocators.BLACK_COLOR_LOCATOR,
            OrderPage.Color.GREY: OrderPageLocators.GREY_COLOR_LOCATOR
        }

        self.find_element_located(OrderPageLocators.RENTAL_PERIOD_LOCATOR).click()
        self.find_element_located(rental_period_locators[rental_period]).click()
        self.find_element_located(color_locators[color]).click()
        self.find_element_located(OrderPageLocators.COMMENT_LOCATOR).send_keys(comment)

    @allure.step('Завершить оформление заказа, проверив его статус')
    def finish_order_creation(self):
        self.find_element_located(OrderPageLocators.ORDER_BUTTON_LOCATOR).click()
        self.find_element_located(OrderPageLocators.ORDER_CONFIRMATION_BUTTON_LOCATOR).click()
        self.find_element_located(OrderPageLocators.CHECK_ORDER_STATUS_LOCATOR).click()

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        order_number = self.find_element_located(OrderPageLocators.ORDER_NUMBER_INPUT_LOCATOR).text
        return order_number

    @allure.step('Нажать на логотип "Самокат"')
    def click_on_scooter_logo(self):
        self.find_element_located(OrderPageLocators.SCOOTER_LOGO_LOCATOR).click()

    @allure.step('Нажать на логотип "Яндекс"')
    def click_on_yandex_logo(self):
        self.find_element_located(OrderPageLocators.YANDEX_LOGO_LOCATOR).click()
