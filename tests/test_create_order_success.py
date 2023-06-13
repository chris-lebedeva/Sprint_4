import allure
from data.urls import Urls
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage


@allure.title('Проверка оформления заказа через кнопку "Заказать" в правом верхнем углу главной страницы')
@allure.description('Нажимаем на кнопку "Заказать" в правом верхнем углу страницы и проходим весь положительный флоу '
                    'оформления заказа с возвратом на главную страницу по клику на логотип "Самокат"')
def test_create_order_by_clicking_on_the_top_button(driver):
    main_page = MainPage(driver)
    main_page.go_to_site()
    main_page.accept_cookies()
    main_page.click_on_top_order_button()
    order_page = OrderPage(driver)
    order_page.fill_in_client_info()
    order_page.fill_in_first_order_details()
    order_page.finish_order_creation()
    order_number = order_page.get_order_number()
    assert order_number in driver.current_url
    order_page.click_on_scooter_logo()
    assert main_page.current_url() == Urls.SCOOTER_MAIN_PAGE_URL


@allure.title('Проверка оформления заказа через кнопку "Заказать" в нижней части главной страницы')
@allure.description('Нажимаем на кнопку "Заказать" в нижней части главной страницы и проходим весь положительный флоу '
                    'оформления заказа с переходом на страницу "Дзен" по клику на логотип "Яндекс"')
def test_create_order_by_clicking_on_the_bottom_button(driver):
    main_page = MainPage(driver)
    main_page.go_to_site()
    main_page.accept_cookies()
    main_page.scroll_to_the_bottom_order_button()
    main_page.click_on_bottom_order_button()
    order_page = OrderPage(driver)
    order_page.fill_in_client_info()
    order_page.fill_in_second_order_details()
    order_page.finish_order_creation()
    order_number = order_page.get_order_number()
    assert order_number in driver.current_url
    order_page.click_on_yandex_logo()
    driver.switch_to.window(driver.window_handles[1])
    main_page.wait_for_dzen_logo(driver)
    assert main_page.current_url() == Urls.DZEN_MAIN_PAGE_URL
