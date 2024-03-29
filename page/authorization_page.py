from selene import browser, have
import allure


class AuthorizationPage:
    with allure.step('Открываем страницу регистрации'):
        def open(self):
            browser.open('/client_account/login')

    with allure.step('Заполняем данные'):
        def fill_email(self, email):
            browser.element('#email').type(email)

        def fill_password(self, password):
            browser.element('#password').type(password)

        with allure.step('Отправляем данные'):
            def fill_entrance(self):
                browser.element('.co-button').click()

            with allure.step('Переходим на страницу с контактными данными'):
                def fill_personal_area(self):
                    browser.element('[href="/client_account/contacts"]').click()
            with allure.step('Проверяем, что пользователь авторизован'):
                def should_contact_details(self, email):
                    browser.element('#client_email').should(have.value(email))

                with allure.step('Проверяем, что пользователь не авторизован'):
                        def should_check_details(self, danger):
                            browser.element('.co-notice--danger').should(have.text(danger))


authorization_page = AuthorizationPage()
