from boroda_land_project_tests.pages.registration_page import registration_page


def test_new_user_registration():
    registration_page.open()

    registration_page.registration_form()
    registration_page.fill_form()

    registration_page.sending_data()

    registration_page.should_must_be_registered()
