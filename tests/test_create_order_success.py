import allure
from data.data import Comments
from data.generators import GeneratedData
from data.urls import Urls
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage


@allure.feature('Оформление заказа')
class TestOrderCreation:

    @allure.title('Проверка оформления заказа через кнопку "Заказать" в правом верхнем углу главной страницы')
    @allure.description('Нажимаем на кнопку "Заказать" в правом верхнем углу страницы и проходим весь положительный '
                        'флоу оформления заказа')
    def test_create_order_by_clicking_on_the_top_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(Urls.SCOOTER_MAIN_PAGE_URL)
        main_page.accept_cookies()
        main_page.click_on_top_order_button()
        order_page = OrderPage(driver)
        first_name = GeneratedData.generate_random_first_name()
        last_name = GeneratedData.generate_random_last_name()
        street_address = GeneratedData.generate_random_street_address()
        phone_number = GeneratedData.generate_random_phone_number()
        order_page.fill_in_client_info(first_name, last_name, street_address, phone_number)
        order_page.fill_in_order_details(OrderPage.RentalPeriod.ONE_DAY, OrderPage.Color.BLACK, Comments.first_comment)
        order_page.finish_order_creation()
        order_number = order_page.get_order_number()
        assert order_number in driver.current_url, 'Не удалось проверить статус заказа, поскольку номер заказа в урле ' \
                                                   'отсутствует либо не соответствует оформленному заказу'

    @allure.title('Проверка оформления заказа через кнопку "Заказать" в нижней части главной страницы')
    @allure.description('Нажимаем на кнопку "Заказать" в нижней части главной страницы и проходим весь положительный '
                        'флоу оформления заказа')
    def test_create_order_by_clicking_on_the_bottom_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(Urls.SCOOTER_MAIN_PAGE_URL)
        main_page.accept_cookies()
        main_page.scroll_to_the_bottom_order_button()
        main_page.click_on_bottom_order_button()
        order_page = OrderPage(driver)
        first_name = GeneratedData.generate_random_first_name()
        last_name = GeneratedData.generate_random_last_name()
        street_address = GeneratedData.generate_random_street_address()
        phone_number = GeneratedData.generate_random_phone_number()
        order_page.fill_in_client_info(first_name, last_name, street_address, phone_number)
        order_page.fill_in_order_details(OrderPage.RentalPeriod.TWO_DAYS, OrderPage.Color.GREY, Comments.second_comment)
        order_page.finish_order_creation()
        order_number = order_page.get_order_number()
        assert order_number in driver.current_url, 'Не удалось проверить статус заказа, поскольку номер заказа в урле ' \
                                                   'отсутствует либо не соответствует оформленному заказу'
