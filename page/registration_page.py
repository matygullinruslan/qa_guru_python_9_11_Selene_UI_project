from selene import browser, have, be, by

class Registration_page:
    def open(self):
        browser.open('/client_account/login')

    def registration_form(self):
        browser.element('[href = "/client_account/contacts/new"]').click()

    def fill_name(self, name):
         browser.element('#client_name').type(name)

    def fill_phone(self, phone):
      browser.element('#client_phone').type(phone)

    def fill_email(self, email):
        browser.element('#client_email').type(email)

    def fill_password(self, password):
        browser.element('#client_password').type(password)

    def fill_password_confirmation(self, confirmation):
         browser.element('#client_password_confirmation').type(confirmation)

    def sending_data(self):
     browser.element('.co-form-button').click()

    def should_name(self, name):
         browser.element('#client_name').should(have.value(name))

    def should_email(self, email):
         browser.element('#client_email').should(have.value(email))

registration_page = Registration_page()


# def test_new_user_registration():
#     browser.open('/client_account/login')
#     browser.element('[href = "/client_account/contacts/new"]').click()
#     browser.element('#client_name').type('Иван')
#     browser.element('#client_phone').type('+7(926)111-11-11')
#     browser.element('#client_email').type('ivan@ivanov.ru')
#     browser.element('#client_password').type('Qwerty987654321')
#     browser.element('#client_password_confirmation').type('Qwerty987654321')
#     browser.element('.co-form-button').click()
#     browser.element('#client_name').should(have.value('Иван'))
#     browser.element('#client_email').should(have.value('ivan@ivanov.ru'))