import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.order_locators import OrderLocators as LOC
from .base_page import BasePage
from selenium.webdriver.common.by import By

class OrderPage(BasePage):
    LOC = LOC

    @allure.step("Заполнить форму личных данных")
    def fill_form_personal(self, first, last, addr, metro, phone):
        self.type(self.LOC.FIRST_NAME, first)
        self.type(self.LOC.LAST_NAME, last)
        self.type(self.LOC.ADDRESS, addr)
        self.click(self.LOC.METRO)
        self.driver.find_element(By.XPATH, f"//div[text()='{metro}']").click()
        self.type(self.LOC.PHONE, phone)
        self.click(self.LOC.NEXT_BTN)

    @allure.step("Заполнить форму аренды")
    def fill_form_rent(self, date_str, duration, color, comment):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOC.DATE)).click()
        self.driver.find_element(
            self.LOC.DATE[0],
            f"//div[contains(@class,'react-datepicker')]//div[text()='{date_str.split('-')[-1]}']"
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(("class name", "react-datepicker__day-name"))
        )
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOC.DURATION)).click()
        self.driver.find_element("xpath", f"//div[@role='option' and text()='{duration}']").click()
        self.click(self.LOC.COLOR_BLACK if color else self.LOC.COLOR_GREY)
        if comment:
            self.type(self.LOC.COMMENT, comment)

    @allure.step("Нажать кнопки 'Заказать' и 'Да'")
    def click_confirm(self):
        self.click(self.LOC.ORDER_CONFIRM)
        self.click(self.LOC.CONFIRM_BTN)
