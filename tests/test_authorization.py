from boroda_land_project_tests.pages.authorization_page import authorization_page


def test_successful_authorization():
    authorization_page.open()

    authorization_page.fill_email()
    authorization_page.fill_successful_password()
    authorization_page.fill_entrance()
    authorization_page.fill_personal_area()

    authorization_page.should_contact_details()


def test_unsuccessful_authorization():
    authorization_page.open()

    authorization_page.fill_email()
    authorization_page.fill_unsuccessful_password()
    authorization_page.fill_entrance()

    authorization_page.should_check_details('Сочетание логина и пароля не подходит')
