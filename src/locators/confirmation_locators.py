from selenium.webdriver.common.by import By

class ConfirmationLocators:
    MODAL        = (By.CSS_SELECTOR, "div.Order_Modal__YZ-d3")
    STATUS_BTN   = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")
    LOGO_SCOOTER = (By.CSS_SELECTOR, "a[class*='Header_LogoScooter']")
    LOGO_YANDEX  = (By.CSS_SELECTOR, "a[class*='Header_LogoYandex']")
