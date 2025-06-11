import pytest
import allure
from src.pages.main_page import MainPage
from src.pages.order_page import OrderPage
from src.pages.confirmation_modal import ConfirmationModal
from src.data.order_data import order_test_data

@allure.suite("Order")
@allure.feature("Order Full Flow")
class TestOrder:

    @allure.title("Позитивный флоу заказа (top={top})")
    @pytest.mark.parametrize("top, first, last, addr, metro, phone, date, duration, color, comment", order_test_data)
    def test_order_full_flow(self, driver, top, first, last, addr, metro, phone, date, duration, color, comment):
        main = MainPage(driver)
        order = OrderPage(driver)
        modal = ConfirmationModal(driver)

        with allure.step("Открыть главную и начать заказ"):
            main.open()
            main.click_order(top)

        with allure.step("Заполнить форму данных и аренды"):
            order.fill_form_personal(first, last, addr, metro, phone)
            order.fill_form_rent(date, duration, color, comment)
            order.click_confirm()

        with allure.step("Ждать подтверждение заказа"):
            assert modal.wait_confirmation(), "Модалка не появилась"

        with allure.step("Нажать 'Посмотреть статус'"):
            modal.click_status()

        with allure.step("Проверить логотип Самоката (вернуться на главную)"):
            modal.click_logo_scooter()
            assert main.is_main_page(), "Не вернулись на главную по лого"

        with allure.step("Проверить логотип Яндекса (откроет Дзен в новой вкладке)"):
            modal.click_logo_yandex()
            main.switch_to_last_window()
            url = main.wait_url_contains("dzen.ru")
            assert "dzen.ru" in url
