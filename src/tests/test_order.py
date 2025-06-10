import pytest
import allure
from src.pages.main_page import MainPage
from src.pages.order_page import OrderPage
from src.pages.confirmation_modal import ConfirmationModal
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.parametrize("top, first, last, addr, metro, phone, date, duration, color, comment", [
    (True,  "Иван",  "Петров",  "Ул. Ленина, д.1",  "Черкизовская", "+79161234567", "2025-06-20", "сутки",     True,  "оставить у двери"),
    (False, "Мария", "Сидорова","Ул. Пушкина, д.10", "Курская",      "+79876543210", "2025-06-21", "двое суток", False, "")
])
@allure.feature("Полный сценарий заказа")
def test_order_full_flow(driver, top, first, last, addr, metro, phone, date, duration, color, comment):
    main = MainPage(driver)
    order = OrderPage(driver)
    modal = ConfirmationModal(driver)

    with allure.step("Открыть главную и начать заказ"):
        main.open()
        main.click_order(top)

    with allure.step("Заполнить форму данных и аренды"):
        order.fill_form_personal(first, last, addr, metro, phone)
        order.fill_form_rent(date, duration, color, comment)

    with allure.step("Подтвердить заказ"):
        order.click_confirm()
        assert modal.wait_confirmation(), "Модалка подтверждения не появилась"

    with allure.step("Нажать кнопку 'Посмотреть статус'"):
        modal.click_status()

    with allure.step("Проверить переход на главную по логотипу Самоката"):
        modal.click_logo_scooter()
        assert main.driver.current_url.rstrip('/') == main.base_url.rstrip('/'), \
            "Логотип Самоката не вернул на главную"

    with allure.step("Открыть заново и проверить логотип Яндекса"):
        modal.click_logo_yandex()
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        WebDriverWait(driver, 10).until(lambda d: "dzen.ru" in d.current_url)
        assert "dzen.ru" in driver.current_url
