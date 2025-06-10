import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from src.locators.main_locators import MainLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    LOC = MainLocators
    base_url = "https://qa-scooter.praktikum-services.ru/"
    
    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        try:
            btn = self.wait.until(EC.element_to_be_clickable(self.LOC.COOKIE_BTN))
            btn.click()
            self.wait.until(EC.invisibility_of_element_located(self.LOC.COOKIE_OVERLAY))
        except:
            pass

    @allure.step("Подтвердить заказ кнопками 'Заказать' и 'Да'")
    def click_order(self, top: bool = True):
        locator = self.LOC.ORDER_TOP if top else self.LOC.ORDER_BOTTOM
        self.click(locator)

    @allure.step("Проверка FAQ вопроса #{idx}")
    def verify_faq_question(self, idx: int, expected_text: str):
        wait = WebDriverWait(self.driver, 10)
        
        locator_q = (By.XPATH, f"(//div[contains(@class,'accordion__heading')])[{idx+1}]")
        locator_p = (By.XPATH, f"(//div[contains(@class,'accordion__panel')])[{idx+1}]")

        el_q = wait.until(EC.element_to_be_clickable(locator_q))
        el_q.location_once_scrolled_into_view  
        wait.until(EC.element_to_be_clickable(locator_q)).click()
        
        el_a = wait.until(EC.visibility_of_element_located(locator_p))
        actual = el_a.text
        assert expected_text in actual, f"FAQ #{idx+1}: ожидали '{expected_text}', получили '{actual}'"