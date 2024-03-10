from selene import browser, have


class Cartpage:
    def open(self):
        browser.open('/')

    def find_cart(self, cart):
        browser.element(by.name('q')).should(be.blank).type(cart).press_enter()

    def choice_item(self):
        browser.element('[href="/product/raz1016-muzhskoy-shampun-dlya-normalnyh-i-zhirnyh-volos-220-ml"]').click()

    def detail_item(self):
        browser.element('#product-detail-buy-area').click()

    def should_item(self, shampoo):
        browser.element('.add-cart-counter__detail-text').should(have.text(shampoo))

    def choice_item(self):
        browser.element('[href="/collection/britie"]').hover()
        browser.element('[href="/collection/britie-sredstva-dlya-britya"]').click()
        browser.element('[href="/product/care143-loson-posle-britya-proraso-sandal-sandal"]').click()

    def added_cart(self):
        browser.element('.add-cart-counter').click()

    def entrance_cart(self):
        browser.element('.header__control-text').click()

    def delete_item(self):
        browser.element('.js-item-delete').click()

    def should_cart(self, text):
        browser.element('.text-center').should(have.text(text))




test_cart_page = Cartpage()


from selene import browser, have, be, by

# def test_added_cart_items():
#     browser.open('/')
#     browser.element(by.name('q')).should(be.blank).type('Шампунь').press_enter()
#     browser.element('[href="/product/raz1016-muzhskoy-shampun-dlya-normalnyh-i-zhirnyh-volos-220-ml"]').click()
#     browser.element('#product-detail-buy-area').click()
#     browser.element('.add-cart-counter__detail-text').should(have.text('В корзине 1 шт'))
