from selene import browser, have, be, by
from page.cart_items_page import test_cart_page
import allure
from time import sleep


def test_added_cart_items():
    test_cart_page.open()
    test_cart_page.find_cart('Шампунь')
    test_cart_page.choice_item()
    test_cart_page.detail_item()
    test_cart_page.should_item('В корзине 1 шт')

def test_delete_cart_items():
    test_cart_page.open()
    #выбор из выпадающего списка категории товара
    test_cart_page.choice_item()
    sleep(7)
    test_cart_page.added_cart()
    sleep(7)
    test_cart_page.entrance_cart()
    sleep(7)
    test_cart_page.delete_item()
    sleep(7)
    test_cart_page.should_cart('Ваша корзина пуста')
...
   #
   #  browser.element('[href="/collection/britie"]').hover()
   #  browser.element('[href="/collection/britie-sredstva-dlya-britya"]').click()
   # #выбор карточки товара
   #  browser.element('[href="/product/care143-loson-posle-britya-proraso-sandal-sandal"]').click()
   # #добавление товара в корзину
   #  browser.element('.add-cart-counter').click()
   #  # переход в корзину
   #  browser.element('.header__control-text').click()
   #  #удаление  товара из корзины
   #  browser.element('.js-item-delete').click()
   #  #проверка, что корзина пуста после удаления товара
   #  browser.element('.text-center').should(have.text('Ваша корзина пуста'))
   #

