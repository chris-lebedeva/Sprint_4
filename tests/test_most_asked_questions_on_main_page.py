import allure
import pytest
from data.urls import Urls
from page_objects.main_page import MainPage
from data.data import Answers


class TestQuestionsAndAnswers:

    @allure.title('Проверка списка часто задаваемых вопросов и ответов на главной странице')
    @allure.description('На главной странице ищем список часто задаваемых вопросов и ответов и проверяем корректность '
                        'ответов')
    @pytest.mark.parametrize("index", range(8))
    def test_most_asked_questions_on_main_page(self, driver, index):
        main_page = MainPage(driver)
        main_page.go_to_site(Urls.SCOOTER_MAIN_PAGE_URL)
        main_page.accept_cookies()
        main_page.scroll_to_the_most_asked_questions_section()
        main_page.click_on_questions(index)
        answer = main_page.get_answers()
        assert answer == Answers.answers[index], f'Получен некорректный текст ответа. Ожидалось: {answer}'
