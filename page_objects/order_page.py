from data.generators import GeneratedData
from locators.order_page_locators import OrderPageLocators
from page_objects.base_page import BasePage
from data.data import Comments


class OrderPageHelper(BasePage):

    def fill_in_client_info(self):
        self.find_element_located(OrderPageLocators.FIRST_NAME_LOCATOR).send_keys(
            GeneratedData.generate_random_first_name())
        self.find_element_located(OrderPageLocators.LAST_NAME_LOCATOR).send_keys(
            GeneratedData.generate_random_last_name())
        self.find_element_located(OrderPageLocators.STREET_ADDRESS_LOCATOR).send_keys(
            GeneratedData.generate_random_street_address())
        self.find_element_located(OrderPageLocators.STATION_LOCATOR).click()
        station = self.find_element_located(OrderPageLocators.REQUIRED_STATION_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView();", station)
        station.click()
        self.find_element_located(OrderPageLocators.PHONE_NUMBER_LOCATOR).send_keys(
            GeneratedData.generate_random_phone_number())
        self.find_element_located(OrderPageLocators.NEXT_BUTTON).click()
        self.find_element_located(OrderPageLocators.RENTAL_DATE_LOCATOR).click()
        next_day = self.find_element_located(OrderPageLocators.NEXT_DAY_LOCATOR)
        excluded_day = self.find_element_located(OrderPageLocators.EXCLUDED_DATE_LOCATOR)

        if next_day == excluded_day:
            self.find_element_located(OrderPageLocators.REPLACED_DATE_LOCATOR).click()
        else:
            next_day.click()

    def fill_in_first_order_details(self):
        self.find_element_located(OrderPageLocators.RENTAL_PERIOD_LOCATOR).click()
        self.find_element_located(OrderPageLocators.ONE_DAY_LOCATOR).click()
        self.find_element_located(OrderPageLocators.BLACK_COLOR_LOCATOR).click()
        self.find_element_located(OrderPageLocators.COMMENT_LOCATOR).send_keys(Comments.first_comment)

    def fill_in_second_order_details(self):
        self.find_element_located(OrderPageLocators.RENTAL_PERIOD_LOCATOR).click()
        self.find_element_located(OrderPageLocators.TWO_DAYS_LOCATOR).click()
        self.find_element_located(OrderPageLocators.GREY_COLOR_LOCATOR).click()
        self.find_element_located(OrderPageLocators.COMMENT_LOCATOR).send_keys(Comments.second_comment)

    def finish_order_creation(self):
        self.find_element_located(OrderPageLocators.ORDER_BUTTON_LOCATOR).click()
        self.find_element_located(OrderPageLocators.ORDER_CONFIRMATION_BUTTON_LOCATOR).click()
        self.find_element_located(OrderPageLocators.CHECK_ORDER_STATUS_LOCATOR).click()

    def get_order_number(self):
        order_number = self.find_element_located(OrderPageLocators.ORDER_NUMBER_INPUT_LOCATOR).text
        return order_number

    def click_on_scooter_logo(self):
        self.find_element_located(OrderPageLocators.SCOOTER_LOGO_LOCATOR).click()

    def click_on_yandex_logo(self):
        self.find_element_located(OrderPageLocators.YANDEX_LOGO_LOCATOR).click()
