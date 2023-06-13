from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_ACCEPT_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'App_CookieButton')]")
    MOST_ASKED_QUESTIONS_SECTION_HEADING_LOCATOR = (By.XPATH, "//div[contains(@class, 'Home_FAQ')]")
    QUESTION_LOCATOR = (By.XPATH, "//div[contains(@class, 'accordion__item')]")
    ANSWER_LOCATOR = (By.XPATH, "//div[contains(@class, 'accordion__panel') and not(@hidden)]")
    TOP_ORDER_BUTTON_LOCATOR = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[contains(@class, "
                                          "'Button_Button__ra12g')]")
    BOTTOM_ORDER_BUTTON_LOCATOR = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[contains(@class, "
                                             "'Button_Button__ra12g')]")
    DZEN_LOGO_LOCATOR = (By.XPATH, "//a[@aria-label='Логотип Дзен']")
