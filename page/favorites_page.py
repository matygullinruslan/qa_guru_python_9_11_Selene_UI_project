from selene import browser, have, be, by


class Added_page:
    def open(self):
        browser.open('/')

    def find_cart(self, cart):
        browser.element(by.name('q')).should(be.blank).type(cart).press_enter()

    def detail_item(self):
        browser.element('.product-preview__title').click()

    def add_to_favorites(self):
        browser.element('.icon-favorites-o').click()

    def entrance_to_favorites(self):
        browser.element('[href="/page/favorites"]').click()

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
