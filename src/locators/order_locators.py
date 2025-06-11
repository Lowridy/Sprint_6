from selenium.webdriver.common.by import By

class OrderLocators:
    FIRST_NAME    = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME     = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS       = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO         = (By.CSS_SELECTOR, ".select-search__input")
    PHONE         = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BTN      = (By.XPATH, "//button[text()='Далее']")
    DATE          = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DURATION      = (By.CSS_SELECTOR, ".Dropdown-control")
    COMMENT       = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    COLOR_BLACK   = (By.ID, "black")
    COLOR_GREY    = (By.ID, "grey")
    ORDER_CONFIRM = (By.XPATH, "//button[contains(text(),'Заказать') and contains(@class,'Button_Middle') and not(contains(@class,'Button_Inverted'))]")
    CONFIRM_BTN   = (By.XPATH, "//button[text()='Да']")

    @staticmethod
    def metro_option(metro):
        return (By.XPATH, f"//div[text()='{metro}']")

    @staticmethod
    def calendar_day(day):
        return (By.XPATH, f"//div[contains(@class,'react-datepicker')]//div[text()='{day}']")

    @staticmethod
    def duration_option(duration):
        return (By.XPATH, f"//div[@role='option' and text()='{duration}']")

    CALENDAR_DAYNAME = (By.CLASS_NAME, "react-datepicker__day-name")
