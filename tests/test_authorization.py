import allure
from page.authorization_page_midle import authorization_page
from selene import browser, have


def test_successful_authorization():
    with allure.step('Открываем страницу регистрации'):
        authorization_page.open()

    with allure.step('Заполняем данные'):
        authorization_page.fill_email('rusel_21@mail.ru')
        authorization_page.fill_password('qwerty123456')

    with allure.step('Отправляем данные'):
        authorization_page.fill_entrance()

    with allure.step('Переходим на страницу с контактными данными'):
        authorization_page.fill_personal_area()

    with allure.step('Проверяем, что пользователь авторизован'):
        authorization_page.should_contact_details(
            'rusel_21@mail.ru',
        )


def test_unsuccessful_authorization():
    with allure.step('Открываем страницу регистрации'):
        authorization_page.open()

    with allure.step('Заполняем данные'):
        authorization_page.email_fill('rusel_21@mail.ru')
        authorization_page.password_fill('123456')


    with allure.step('Отправляем данные'):
        authorization_page.entrance_fill()

    with allure.step('Проверяем, что пользователь не авторизован'):
        authorization_page.should_check_details('Сочетание логина и пароля не подходит')




# def test_unsuccessful_authorization():
#     browser.open('/client_account/login')
#     browser.element('#email').type('rusel_21@mail.ru')
#     browser.element('#password').type('123456')
#     browser.element('.co-button').click()
#     browser.element('.co-notice--danger').should(have.text('Сочетание логина и пароля не подходит'))