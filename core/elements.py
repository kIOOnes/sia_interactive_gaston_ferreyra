from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Elements:

    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))


    def find_in_shadow_chain(self, host_locator, chain):
        host = self.find_element(host_locator)

        current = host

        for by, selector in chain:

            shadow_root = self.driver.execute_script(
                "return arguments[0].shadowRoot",
                current
            )

            if not shadow_root:
                raise NoSuchElementException("ShadowRoot not found")

            current = shadow_root.find_element(by, selector)

        return current

    def send_keys_shadow_chain(self, host_locator, chain, text):

        element = self.find_in_shadow_chain(host_locator, chain)

        self.driver.execute_script("arguments[0].focus();", element)

        try:
            element.clear()
        except Exception:
            pass

        element.send_keys(text)