from selenium.webdriver.common.by import By

class MainLocators:
    COOKIE_BTN     = (By.ID, "rcc-confirm-button")
    COOKIE_OVERLAY = (By.CLASS_NAME, "App_CookieConsent__1yUIN")
    FAQ_QUESTION   = (By.XPATH, "(//div[contains(@class,'accordion__heading')])[{n}]")
    FAQ_PANEL      = (By.XPATH, "(//div[contains(@class,'accordion__panel')])[{n}]")
    ORDER_TOP      = (By.CSS_SELECTOR, ".Button_Button__ra12g")
    ORDER_BOTTOM   = (By.CSS_SELECTOR, ".Button_Button__ra12g.Button_UltraBig__UU3Lp")
