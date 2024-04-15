from page.registration_page import registration_page


def test_new_user_registration():
    registration_page.open()

    registration_page.registration_form()
    registration_page.fill_name()
    registration_page.fill_phone()
    registration_page.fill_email()
    registration_page.fill_password()
    registration_page.fill_password_confirmation()

    registration_page.sending_data()

    registration_page.should_name()
    registration_page.should_email()

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
