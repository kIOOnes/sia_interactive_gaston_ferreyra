from core.elements import Elements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

USERNAME_HOST = (By.CSS_SELECTOR, "dex-app")

USERNAME_CHAIN = [
    (By.CSS_SELECTOR, "dex-login"),
    (By.CSS_SELECTOR, "paper-input#username"),
    (By.CSS_SELECTOR, "iron-input input")
]

PASSWORD_CHAIN = [
    (By.CSS_SELECTOR, "dex-login"),
    (By.CSS_SELECTOR, "paper-input#password"),
    (By.CSS_SELECTOR, "iron-input input")
]

LOGIN_BUTTON = (By.XPATH,"//paper-button[contains(@class,'login-btn') and contains(normalize-space(),'Iniciar')]")

DASHBOARD_TITLE = (By.ID, "pageTitle")


class landingLoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.elm = Elements(driver)
        WebDriverWait(driver, 60).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
)

    def enter_username(self, username):
        self.elm.send_keys_shadow_chain(USERNAME_HOST,USERNAME_CHAIN,username)

    def enter_password(self, password):
        self.elm.send_keys_shadow_chain(USERNAME_HOST,PASSWORD_CHAIN,password)

    def submit_login(self):

        self.driver.execute_script("""
            let buttons = document.querySelectorAll("paper-button");

            for (let btn of buttons){

                let text = btn.innerText || "";

                if (text.toLowerCase().includes("iniciar")){

                    btn.scrollIntoView({block:'center'});

                    btn.dispatchEvent(new MouseEvent('mousedown', {bubbles:true}));
                    btn.dispatchEvent(new MouseEvent('mouseup', {bubbles:true}));
                    btn.dispatchEvent(new MouseEvent('click', {bubbles:true}));

                    return true;
                }
            }

            return false;
        """)

        self.driver.execute_script("""
        document.querySelector("form").requestSubmit();
        """)

    def success_title(self):
        return self.elm.find_element(DASHBOARD_TITLE).text