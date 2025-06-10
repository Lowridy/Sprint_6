import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import driver
from .base_page import BasePage
from src.locators.confirmation_locators import ConfirmationLocators
from selenium.webdriver.common.by import By

class ConfirmationModal(BasePage):
    LOC = ConfirmationLocators

    @allure.step("Ожидание появления модального окна")
    def wait_confirmation(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LOC.MODAL)
        )

    @allure.step("Нажать кнопку 'Посмотреть статус'")
    def click_status(self):
        self.click(self.LOC.STATUS_BTN)
        # ЖДЁМ исчезновения оверлея после клика!
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "Order_Overlay__3KW-T"))
        )

    @allure.step("Нажать логотип Самоката")
    def click_logo_scooter(self):
        self.click(self.LOC.LOGO_SCOOTER)

    @allure.step("Нажать логотип Яндекса")
    def click_logo_yandex(self):
        self.driver.save_screenshot('before_logo_click.png')
        self.click(self.LOC.LOGO_YANDEX)

