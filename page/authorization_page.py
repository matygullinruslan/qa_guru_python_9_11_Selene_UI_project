from selene import browser, have


class AuthorizationPage:

    def open(self):
        browser.open('/client_account/login')

    def fill_email(self, email):
        browser.element('#email').type(email)

    def fill_password(self, password):
        browser.element('#password').type(password)

    def fill_entrance(self):
        browser.element('.co-button').click()

    def fill_personal_area(self):
        browser.element('[href="/client_account/contacts"]').click()

    def should_contact_details(self, email):
        browser.element('#client_email').should(have.value(email))

    def should_check_details(self, danger):
        browser.element('.co-notice--danger').should(have.text(danger))

authorization_page = AuthorizationPage()
