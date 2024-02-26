# import allure
from selene import browser, have


def test_new_user_registration():
    browser.open('/client_account/login')
    browser.element('[href = "/client_account/contacts/new"]').click()
    browser.element('#client_name').type('Иван')
    browser.element('#client_phone').type('+7(926)111-11-11')
    browser.element('#client_email').type('ivan@ivanov.ru')
    browser.element('#client_password').type('Qwerty987654321')
    browser.element('#client_password_confirmation').type('Qwerty987654321')
    browser.element('.co-form-button').click()
    browser.element('#client_name').should(have.value('Иван'))
    browser.element('#client_email').should(have.value('ivan@ivanov.ru'))



