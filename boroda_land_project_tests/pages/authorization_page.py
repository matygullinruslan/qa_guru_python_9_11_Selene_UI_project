from selene import browser, have
import allure
from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('AUTH_SUCCESSFUL_PASSWORD')
wrong_password = os.getenv('AUTH_UNSUCCESSFUL_PASSWORD')


class AuthorizationPage:

    def open(self):
        with allure.step('Открываем страницу регистрации'):
            browser.open('/client_account/login')

    def fill_email(self):
        with allure.step('Вводим email'):
            browser.element('#email').type(email)

    def fill_successful_password(self):
        with allure.step('Вводим пароль'):
            browser.element('#password').type(password)

    def fill_unsuccessful_password(self):
        with allure.step('Вводим неверный пароль'):
            browser.element('#password').type(wrong_password)

    def fill_entrance(self):
        with allure.step('Отправляем данные'):
            browser.element('.co-button').click()

    def fill_personal_area(self):
        with allure.step('Переходим на страницу с контактными данными'):
            browser.element('[href="/client_account/contacts"]').click()

    def should_contact_details(self):
        with allure.step('Проверяем, что пользователь авторизован'):
            browser.element('#client_email').should(have.value(email))

    def should_check_details(self, danger):
        with allure.step('Проверяем, что пользователь не авторизован'):
            browser.element('.co-notice--danger').should(have.text(danger))


authorization_page = AuthorizationPage()
