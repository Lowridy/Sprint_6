import allure
from src.locators.confirmation_locators import ConfirmationLocators
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ConfirmationModal(BasePage):
    LOC = ConfirmationLocators

    @allure.step("Ожидание модального окна")
    def wait_confirmation(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LOC.MODAL)
        )

    @allure.step("Нажать кнопку 'Посмотреть статус'")
    def click_status(self):
        self.click(self.LOC.STATUS_BTN)

    @allure.step("Нажать логотип Самоката")
    def click_logo_scooter(self):
        self.click(self.LOC.LOGO_SCOOTER)

    @allure.step("Нажать логотип Яндекса")
    def click_logo_yandex(self):
        self.click(self.LOC.LOGO_YANDEX)
