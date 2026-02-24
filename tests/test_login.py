import pytest
from pages.login_pages.landing_login_page import landingLoginPage
import time

def test_login_correctly(driver):

    # -------------------------
    # A-A-A TEST DESIGN PATTERN (Arrange, Act, Assert)
    # Arrange
    # -------------------------
    

    login_page = landingLoginPage(driver)

    # -------------------------
    # Act
    # -------------------------

    login_page.enter_username("challengeqa")
    login_page.enter_password("Abcd1234")

    login_page.submit_login()
    login_page.submit_login()

    # -------------------------
    # Assert
    # -------------------------

    assert login_page.success_title() == "Dashboard"