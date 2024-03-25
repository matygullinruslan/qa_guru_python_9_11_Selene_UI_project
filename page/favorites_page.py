import allure
from selene import browser, have, be, by


class Added_page:
    with allure.step('Открываем сайт'):
        def open(self):
            browser.open('/')

    with allure.step('В поисковой строке вводим наименование нужного товара'):
        def find_cart(self, cart):
            browser.element(by.name('q')).should(be.blank).type(cart).press_enter()

    with allure.step('Открываем карточку товара'):
        def detail_item(self):
            browser.element('.product-preview__title').click()

    with allure.step('Добавляем товар в избранное'):
        def add_to_favorites(self):
            browser.element('.icon-favorites-o').click()

    with allure.step('Переходим на вкладку избранное'):
        def entrance_to_favorites(self):
            browser.element('[href="/page/favorites"]').click()

    with allure.step('Проверяем, что товар добавлен в "Избранное"'):
        def should_to_favorites(self, text):
            browser.element('.static-text').should(have.text(
            'text'))
 #тест не проходит из-за баги,
 # после добавления товара в избранное он не отображается на вкладке "Избранное"

favorites_page = Added_page()

#
# def test_added_page_favorites():
#     browser.open('/')
#     browser.element(by.name('q')).should(be.blank).type('Поясная сумка').press_enter()
#     browser.element('.product-preview__title').click()
#     browser.element('.icon-favorites-o').click()
#     browser.element('[href="/page/favorites"]').click()
#     browser.element('.static-text').should(have.text(
#             'BAG379-3 Мужская поясная сумка ручной работы их натуральной кожи'))
