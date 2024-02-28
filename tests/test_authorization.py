import allure
# from page.authorization_page_midle import authorization_page

from selene import browser, have


def test_successful_authorization():
    with allure.step('Открываем страницу регистрации'):
        browser.open('/client_account/login')

    with allure.step('Заполняем форму авторизации'):
        browser.element('#email').type('rusel_21@mail.ru')
        browser.element('#password').type('qwerty123456')

    with allure.step('Отправляем данные'):
        browser.element('.co-button').click()

    with allure.step('Открываем страницу регистрации'):
        browser.element('[href="/client_account/contacts"]').click()

    with allure.step('Проверяем, что пользователь авторизован'):
        browser.element('#client_name').should(have.value('Руслан Матыгуллин'))

def test_unsuccessful_authorization():
    browser.open('/client_account/login')
    browser.element('#email').type('rusel_21@mail.ru')
    browser.element('#password').type('123456')
    browser.element('.co-button').click()
    browser.element('.co-notice--danger').should(have.text('Сочетание логина и пароля не подходит'))

