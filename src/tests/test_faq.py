import pytest
import allure
from src.pages.main_page import MainPage
from src.data.faq_data import faq_data

@allure.suite("FAQ Блок")
@allure.feature("FAQ — Автоскролл и проверка контента")
class TestFAQ:
    @allure.title("Проверка вопроса FAQ #{idx}")
    @pytest.mark.parametrize("idx, expected", faq_data)
    def test_each_faq_question(self, driver, idx, expected):
        main = MainPage(driver)
        main.open()
        main.verify_faq_question(idx, expected)
