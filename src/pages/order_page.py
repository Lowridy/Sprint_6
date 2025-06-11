import allure
from src.locators.order_locators import OrderLocators
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage(BasePage):
    LOC = OrderLocators

    @allure.step("Заполнить личные данные")
    def fill_form_personal(self, first, last, addr, metro, phone):
        self.type(self.LOC.FIRST_NAME, first)
        self.type(self.LOC.LAST_NAME, last)
        self.type(self.LOC.ADDRESS, addr)
        self.click(self.LOC.METRO)
        self.click(self.LOC.metro_option(metro))
        self.type(self.LOC.PHONE, phone)
        self.click(self.LOC.NEXT_BTN)

    @allure.step("Заполнить параметры аренды")
    def fill_form_rent(self, date_str, duration, color, comment):
        self.click(self.LOC.DATE)
        day = date_str.split('-')[-1]
        self.click(self.LOC.calendar_day(day))
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(self.LOC.CALENDAR_DAYNAME))
        self.click(self.LOC.DURATION)
        self.click(self.LOC.duration_option(duration))
        self.click(self.LOC.COLOR_BLACK if color else self.LOC.COLOR_GREY)
        if comment:
            self.type(self.LOC.COMMENT, comment)

    @allure.step("Подтвердить заказ")
    def click_confirm(self):
        self.click(self.LOC.ORDER_CONFIRM)
        self.click(self.LOC.CONFIRM_BTN)
