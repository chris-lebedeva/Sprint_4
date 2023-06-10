import allure
from page_objects.main_page import MainPageHelper
from data.data import Answers


@allure.title('Проверка списка часто задаваемых вопросов и ответов на главной странице')
@allure.description('На главной странице ищем список часто задаваемых вопросов и ответов и проверяем корректность '
                    'ответов')
def test_most_asked_questions_on_main_page(driver):
    main_page = MainPageHelper(driver)
    main_page.go_to_site()
    main_page.accept_cookies()
    main_page.scroll_to_the_most_asked_questions_section()
    answers = main_page.click_on_questions_get_answers(driver)
    assert answers == Answers.answers
