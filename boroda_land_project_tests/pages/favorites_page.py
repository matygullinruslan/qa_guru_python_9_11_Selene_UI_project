import allure
from selene import browser, have, be, by


class AddedPage:

    def open(self):
        with allure.step('Открываем сайт'):
            browser.open('/')

    def find_cart(self, cart):
        with allure.step('В поисковой строке вводим наименование нужного товара'):
            browser.element(by.name('q')).should(be.blank).type(cart).press_enter()

    def detail_item(self):
        with allure.step('Открываем карточку товара'):
            browser.element('.product-preview__title').click()

    def add_to_favorites(self):
        with allure.step('Добавляем товар в избранное'):
            browser.element('.icon-favorites-o').click()
            browser.element('.micro-alert-item').should(be.visible).should(have.text('Товар добавлен в избранное'))

    def entrance_to_favorites(self):
        with allure.step('Переходим на вкладку избранное'):
            browser.element('[href="/pages/favorites"]').click()

    def should_to_favorites(self, text):
        with allure.step('Проверяем, что товар добавлен в "Избранное"'):
            browser.element('.static-text').should(have.text(
                text))


favorites_page = AddedPage()
