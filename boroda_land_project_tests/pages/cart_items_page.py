from selene import browser, have, be, by, command
import allure


class CartPage:

    def open(self):
        with allure.step('Открываем сайт'):
            browser.open('/')

    def find_cart(self, cart):
        with allure.step('Вводим в поисковой строке наименование товара'):
            browser.element(by.name('q')).should(be.blank).type(cart).press_enter()

    def detail_item(self):
        with allure.step('Добавляем товар в корзину'):
            browser.element('#product-detail-buy-area').click()

    def should_item(self, shampoo):
        with allure.step('Проверяем, что товар добавлен в корзину'):
            browser.element('.add-cart-counter__detail-text').should(have.text(shampoo))

    def choice_item(self):
        with allure.step('Выбор товара из выпадающего списка'):
            browser.element('[href="/collection/britie"]').hover()
            browser.element('[href="/collection/britie-sredstva-dlya-britya"]').click()
            browser.element('[href="/product/raz400111-krem-dlya-britya-150ml-evkalipt"]').click()

    def added_cart(self):
        with allure.step('Добавление товара в корзину'):
            browser.element('.add-cart-counter').should(be.visible).click()
            browser.element('.micro-alert-item').should(be.visible).should(have.text('Товар добавлен в корзину'))

    def entrance_cart(self):
        with allure.step('Переходим в корзину и удаляем товар'):
            browser.element('.add-cart-counter__detail-text').should(have.text('В корзине'))
            browser.element('.header__cart').click()

    def delete_item(self):
        with allure.step('Удаляем товар из корзины'):
            browser.element('.cart-item').with_(timeout=5).should(be.visible)
            browser.element('.js-item-delete').should(be.visible).perform(command.js.click())

    def should_cart(self, text):
        with allure.step('Проверяем, что корзина пуста'):
            browser.element('.cart-item').should(be.not_.visible)
            browser.element('.text-center').should(have.text(text))


cart_page = CartPage()
