import allure
from data.urls import Urls
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage


@allure.feature('Переход по ссылкам')
class TestLogoRedirection:

    @allure.title('Проверка корректности редиректа при клике на логотип "Самокат"')
    @allure.description('Открываем страницу оформления заказа, нажимаем на логотип "Самокат" в левом верхнем углу '
                        'страницы, в результате происходит редирект на главную страницу "Яндекс.Самокат"')
    def test_scooter_redirection_success(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE_URL)
        order_page.click_on_scooter_logo()
        assert order_page.current_url() == Urls.SCOOTER_MAIN_PAGE_URL, 'Произошёл некорректный редирект на главную ' \
                                                                       'страницу "Яндекс.Самокат"'

    @allure.title('Проверка корректности редиректа при клике на логотип "Яндекс"')
    @allure.description('Открываем главную страницу "Яндекс.Самокат", нажимаем на логотип "Яндекс" в левом верхнем '
                        'углу страницы, в результате происходит редирект на страницу "Дзен"')
    def test_yandex_redirection_success(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(Urls.SCOOTER_MAIN_PAGE_URL)
        order_page = OrderPage(driver)
        order_page.click_on_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])
        main_page.wait_for_dzen_logo()
        assert main_page.current_url() == Urls.DZEN_MAIN_PAGE_URL, 'Произошёл некорректный редирект на страницу "Дзен"'
