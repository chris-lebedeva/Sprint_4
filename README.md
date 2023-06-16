# Проект автоматизации тестирования сервиса "Яндекс.Самокат"
1. Основа для написания автотестов — фреймворк pytest
2. Программная библиотека для управления браузерами - Selenium WebDriver
3. Установить зависимости — pip install -r requirements.txt
4. Команда для запуска — pytest -v
5. Автотесты запускаются в браузере Firefox 💜
6. Создать отчёты в Allure — pytest tests --alluredir="allure_results"
7. Просмотреть отчёты Allure — allure serve allure_results
# Тестовые сценарии
1. Выпадающий список в разделе «Вопросы о важном». Проверяется список часто задаваемых вопросов и ответов на главной странице сервиса.
2. Позитивный сценарий оформления заказа через верхнюю кнопку "Заказать" на главной странице.
3. Позитивный сценарий оформления заказа через нижнюю кнопку "Заказать" на главной странице.