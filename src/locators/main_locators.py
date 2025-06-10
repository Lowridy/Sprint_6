from selenium.webdriver.common.by import By

class MainLocators:
    COOKIE_BTN = (By.XPATH, "//*[@id='rcc-confirm-button']")
    COOKIE_OVERLAY = (By.CLASS_NAME, "App_CookieConsent__1yUIN")
    FAQ_QUESTIONS = (By.CSS_SELECTOR, ".accordion__heading")
    FAQ_PANELS = (By.CSS_SELECTOR, ".accordion__panel")
    ORDER_TOP = (By.CSS_SELECTOR, ".Button_Button__ra12g")
    ORDER_BOTTOM = (By.CSS_SELECTOR, ".Button_Button__ra12g.Button_UltraBig__UU3Lp")
