import allure
from .base_page import BasePage
from src.locators.main_locators import MainLocators

class MainPage(BasePage):
    LOC = MainLocators

    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        try:
            self.click(self.LOC.COOKIE_BTN)
        except:
            pass

    @allure.step("Нажать кнопку заказа (top/bottom)")
    def click_order(self, top=True):
        locator = self.LOC.ORDER_TOP if top else self.LOC.ORDER_BOTTOM
        self.click(locator)

    @allure.step("Проверить вопрос FAQ {idx}")
    def verify_faq_question(self, idx, expected_text):
        locator_q = (self.LOC.FAQ_QUESTION[0], self.LOC.FAQ_QUESTION[1].format(n=idx+1))
        locator_p = (self.LOC.FAQ_PANEL[0], self.LOC.FAQ_PANEL[1].format(n=idx+1))
        el_q = self.driver.find_element(*locator_q)
        el_q.click()
        el_a = self.driver.find_element(*locator_p)
        actual = el_a.text
        assert expected_text in actual, f"FAQ #{idx}: ожидали '{expected_text}', получили '{actual}'"

    def is_main_page(self):
        return self.current_url.rstrip('/') == "https://qa-scooter.praktikum-services.ru"
