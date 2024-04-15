from selene import browser, have, be, by, command
import allure


class Cartpage:
    with allure.step('Открываем сайт'):
        def open(self):
            browser.open('/')

    with allure.step('Вводим в поисковой строке наименование товара'):
        def find_cart(self, cart):
            browser.element(by.name('q')).should(be.blank).type(cart).press_enter()

    with allure.step('Добавляем товар в корзину'):
        def detail_item(self):
            browser.element('#product-detail-buy-area').click()

    with allure.step('Проверяем, что товар добавлен в корзину'):
        def should_item(self, shampoo):
            browser.element('.add-cart-counter__detail-text').should(have.text(shampoo))

    with allure.step('Выбор товара из выпадающего списка'):
        def choice_item(self):
            browser.element('[href="/collection/britie"]').hover()
            browser.element('[href="/collection/britie-sredstva-dlya-britya"]').click()
            browser.element('[href="/product/raz400111-krem-dlya-britya-150ml-evkalipt"]').click()

    with allure.step('Добавление товара в корзину'):
        def added_cart(self):
            browser.element('.add-cart-counter').should(be.visible).click()
            browser.element('.micro-alert-item').should(be.visible).should(have.text('Товар добавлен в корзину'))

    with allure.step('Переходим в корзину и удаляем товар'):
        def entrance_cart(self):
            browser.element('.add-cart-counter__detail-text').should(have.text('В корзине'))
            browser.element('.header__cart').click()

    with allure.step('Удаляем товар из корзины'):
        def delete_item(self):
            browser.element('.cart-item').with_(timeout=5).should(be.visible)
            browser.element('.js-item-delete').should(be.visible).perform(command.js.click())

        with allure.step('Проверяем, что корзина пуста'):
            def should_cart(self, text):
                browser.element('.cart-item').should(be.not_.visible)
                browser.element('.text-center').should(have.text(text))


test_cart_page = Cartpage()
