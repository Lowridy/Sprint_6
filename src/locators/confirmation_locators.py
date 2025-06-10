from selenium.webdriver.common.by import By

class ConfirmationLocators:
    MODAL         = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    LOGO_SCOOTER  = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")
    LOGO_YANDEX   = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")
    STATUS_BTN    = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")
