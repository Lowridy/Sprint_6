from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(lambda d: d.find_element(*locator).is_enabled())
        self.driver.find_element(*locator).click()

    def type(self, locator, text):
        el = self.wait.until(lambda d: d.find_element(*locator))
        el.clear()
        el.send_keys(text)

    def wait_visible(self, locator):
        return self.wait.until(lambda d: d.find_element(*locator).is_displayed())

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @property
    def current_url(self):
        return self.driver.current_url

    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda d: text in d.current_url)
        return self.driver.current_url
