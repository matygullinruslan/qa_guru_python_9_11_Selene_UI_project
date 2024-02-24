# import allure
from selene import browser, have


def test_registration():
    browser.open('/client_account/login')
    browser.element('[href = "/client_account/contacts/new"]').click()


...
