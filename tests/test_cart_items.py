from boroda_land_project_tests.pages.cart_items_page import cart_page
import pytest


def test_added_cart_items():
    cart_page.open()

    cart_page.choice_item()
    cart_page.added_cart()

    cart_page.should_item('В корзине 1 шт')


@pytest.mark.xfail(reason='Карточка товара не удаляется')
def test_delete_cart_items():

    cart_page.open()

    cart_page.choice_item()
    cart_page.added_cart()
    cart_page.entrance_cart()
    cart_page.delete_item()

    cart_page.should_cart('Ваша корзина пуста')
