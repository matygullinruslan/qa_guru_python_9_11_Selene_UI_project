import allure
# from page.authorization_page_midle import authorization_page

from selene import browser, have

def test_authorization():
    browser.open('/client_account/login')
    browser.element('#email').type('rusel_21@mail.ru')
    browser.element('#password').type('qwerty123456')
    browser.element('.co-button').click()
    browser.element('[href="/client_account/contacts"]').click()
    browser.element('#client_name').should(have.value('Руслан Матыгуллин'))
    browser.element('#client_email').should(have.value('rusel_21@mail.ru'))


def test_authorization():
    browser.open('/client_account/login')
    browser.element('#email').type('rusel_21@mail.ru')
    browser.element('#password').type('qwerty12345')
    browser.element('.co-button').click()
    browser.element('.co-notice--danger').should(have.text('Сочетание логина и пароля не подходит'))



# class Authorizationpage:
#     pass
#
#
# def test_authorization_midle():
#     with allure.step('Открываем страницу авторизации'):
#         authorization_page.open()
#
#     with (allure.step('Вводим логин и пароль')):
#         authorization_page.fill_email('rusel_21@mail.ru')
#         authorization_page.fill_password('qwerty123456')
#
#     with allure.step('Проверяем что пользователь авторизовался'):
#         authorization_page.fill_contact_details('Руслан Матыгуллин')
#         authorization_page.fill_contact_details('rusel_21@mail.ru')


