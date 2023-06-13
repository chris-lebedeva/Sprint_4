from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIRST_NAME_LOCATOR = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_LOCATOR = (By.XPATH, "//input[@placeholder='* Фамилия']")
    STREET_ADDRESS_LOCATOR = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    STATION_LOCATOR = (By.XPATH, "//input[@placeholder='* Станция метро']")
    REQUIRED_STATION_LOCATOR = (By.XPATH, "//ul/li/button[@value='103']")
    PHONE_NUMBER_LOCATOR = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_NextButton')]/button[contains(@class, "
                             "'Button_Button__ra12g')]")
    RENTAL_DATE_LOCATOR = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    NEXT_DAY_LOCATOR = (By.XPATH, "//div[contains(@class, 'day--today')]/following-sibling::div")
    EXCLUDED_DATE_LOCATOR = (By.XPATH, "//div[contains(@aria-label,'воскресенье')]")
    REPLACED_DATE_LOCATOR = (By.XPATH, "//div[contains(@aria-label,'понедельник')]")
    RENTAL_PERIOD_LOCATOR = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    ONE_DAY_LOCATOR = (By.XPATH, "//div[contains(text(), 'сутки')]")
    TWO_DAYS_LOCATOR = (By.XPATH, "//div[contains(text(), 'двое суток')]")
    BLACK_COLOR_LOCATOR = (By.ID, "black")
    GREY_COLOR_LOCATOR = (By.ID, "grey")
    COMMENT_LOCATOR = (By.XPATH, "//div[contains(@class, 'Input_InputContainer')]/input[contains(@class, "
                                 "'Input_Input__1iN_Z Input_Responsible__1jDKN')]")
    ORDER_BUTTON_LOCATOR = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[@class='Button_Button__ra12g "
                                      "Button_Middle__1CSJM']")
    ORDER_CONFIRMATION_BUTTON_LOCATOR = (By.XPATH, "//button[contains(text(),'Да')]")
    CHECK_ORDER_STATUS_LOCATOR = (By.XPATH, "//button[contains(text(), 'Посмотреть статус')]")
    ORDER_NUMBER_INPUT_LOCATOR = (By.XPATH, "//div[contains(@class, 'Input_InputContainer')]/input[contains(@class, "
                                            "'Input_Input__1iN_Z Track_Input')]")
    SCOOTER_LOGO_LOCATOR = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO_LOCATOR = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
