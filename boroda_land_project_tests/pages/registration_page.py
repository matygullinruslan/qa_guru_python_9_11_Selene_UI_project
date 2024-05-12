import allure
from selene import browser, have
from dotenv import load_dotenv
import os


load_dotenv()

name = os.getenv('NAME')
phone = os.getenv('PHONE')
email = os.getenv('REGISTRATION_EMAIL')
password = os.getenv('REGISTRATION_PASSWORD')
password_confirmation = os.getenv('REGISTRATION_PASSWORD')


class RegistrationPage:
    def open(self):
        with allure.step('Открываем сайт'):
            browser.open('/client_account/login')

    def registration_form(self):
        with allure.step('Переходим на форму регистрации'):
            browser.element('[href = "/client_account/contacts/new"]').click()

    def fill_form(self):
        with allure.step('Заполняем данные для регистрации'):
            browser.element('#client_name').type(name)
            browser.element('#client_phone').type(phone)
            browser.element('#client_email').type(email)
            browser.element('#client_password').type(password)
            browser.element('#client_password_confirmation').type(password_confirmation)

    def sending_data(self):
        with allure.step('Отправляем данные'):
            browser.element('.co-form-button').click()

    def should_must_be_registered(self):
        with allure.step('Проверяем, что пользователь зарегистрирован'):
            browser.element('#client_name').should(have.value(name))
            browser.element('#client_email').should(have.value(email))


registration_page = RegistrationPage()
