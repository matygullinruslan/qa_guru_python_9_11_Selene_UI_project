from selene import browser, have


class RegistrationPage:
    pass


class RegistrationPage:

    def open(self):
        browser.open('/client_account/login')

    def fill_email(self, email):
        browser.element('#email').type(email)

    def fill_password(self, password):
        browser.element('#password').type(password)

    def fill_contact_details(self, contact_name, contract_email):
        browser.element('#client_name').should(have.value(contact_name))
        browser.element('#client_email').should(have.value(contract_email))

    registration_page = RegistrationPage()

#     def authorized_user_with(self, email):
#         browser.element('#userEmail').type(email)
#
#     def fill_gender(self):
#         browser.element('.custom-control').click()
#
#     def fill_phone(self, phone):
#         browser.element('#userNumber').type(phone)
#
#     def fill_date(self, birthday_day, birthday_month, birthday_year):
#         browser.element('#dateOfBirthInput').click()
#         browser.element('.react-datepicker__year-select').click().element(by.text(birthday_year)).click()
#         browser.element('.react-datepicker__month-select').click().element(by.text(birthday_month)).click()
#         browser.element(f'.react-datepicker__day--0{birthday_day}').click()
#         return self
#     def fill_subjects(self, subject):
#         browser.element('#subjectsInput').type(subject).press_enter()
#
#     def fill_hobbies(self):
#         browser.element('[for="hobbies-checkbox-1"]').click()
#
#     def fill_upload_file(self, picture):
#         browser.element('#uploadPicture').send_keys(resource.path(picture))
#
#     def fill_address(self, address):
#         browser.element('#currentAddress').type(address)
#
#     def fill_state(self):
#         browser.element('#state').perform(command.js.scroll_into_view).click()
#         browser.element('#react-select-3-option-0').click()
#
#     def fill_city(self):
#         browser.element('#city').click()
#         browser.element('#react-select-4-option-1').click()
#
#     def fill_submit(self):
#         browser.element('#submit').perform(command.js.click)
#
#     def should_registered_user_with(self, full_name, email, gender, phone, date, subject, hobby, upload_file, address,
#                                     state_city):
#         browser.element('.table').all('td').even.should(have.exact_texts(full_name,
#                                                                          email,
#                                                                          gender,
#                                                                          phone,
#                                                                          date,
#                                                                          subject,
#                                                                          hobby,
#                                                                          upload_file,
#                                                                          address,
#                                                                          state_city
#                                                                          ))
#
#
