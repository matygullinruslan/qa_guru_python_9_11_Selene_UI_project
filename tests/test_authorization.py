from page.authorization_page import authorization_page


def test_successful_authorization():
    authorization_page.open()

    authorization_page.fill_email('rusel_21@mail.ru')
    authorization_page.fill_password('qwerty123456')

    authorization_page.fill_entrance()

    authorization_page.fill_personal_area()

    authorization_page.should_contact_details(
        'rusel_21@mail.ru',
    )


def test_unsuccessful_authorization():

    authorization_page.open()

    authorization_page.fill_email('rusel_21@mail.ru')
    authorization_page.fill_password('123456')

    authorization_page.fill_entrance()

    authorization_page.should_check_details('Сочетание логина и пароля не подходит')

