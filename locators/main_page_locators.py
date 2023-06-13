from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_ACCEPT_BUTTON_LOCATOR = (By.CLASS_NAME, "App_CookieButton__3cvqF")
    MOST_ASKED_QUESTIONS_SECTION_HEADING_LOCATOR = (By.CLASS_NAME, "Home_FourPart__1uthg")
    QUESTION_LOCATOR = (By.XPATH, "//div[@class='accordion__item' ]")
    ANSWER_LOCATOR = (By.XPATH, "//div[contains(@class, 'accordion__panel') and not(@hidden)]")
    TOP_ORDER_BUTTON_LOCATOR = (By.CLASS_NAME, "Button_Button__ra12g")
    BOTTOM_ORDER_BUTTON_LOCATOR = (By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']")
    DZEN_LOGO_LOCATOR = (By.XPATH, "//a[@aria-label='Логотип Дзен']")
