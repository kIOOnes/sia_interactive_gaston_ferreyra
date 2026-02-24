import pytest
from pages.login_pages.landing_login_page import landingLoginPage
import time
from utils.json_loader import load_json

def test_login_correctly(driver):

    data = load_json("data/credentials.json")

    # -------------------------
    # A-A-A TEST DESIGN PATTERN (Arrange, Act, Assert)
    # Arrange
    # -------------------------
    

    login_page = landingLoginPage(driver)

    # -------------------------
    # Act
    # -------------------------

    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.submit_login()

    # -------------------------
    # Assert
    # -------------------------

    assert login_page.success_title() == "Dashboard"