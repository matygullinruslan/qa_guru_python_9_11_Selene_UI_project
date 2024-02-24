from selene import browser,  have


def test_authorization():
    browser.open('/client_account/login')
    browser.element('#email').type('rusel_21@mail.ru')
    browser.element('#password').type('qwerty12345')
    browser.element('.co-button').click()
    browser.element('.co-notice--danger').should(have.text('Сочетание логина и пароля не подходит'))
    ...
