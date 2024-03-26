from page.cart_items_page import test_cart_page


def test_added_cart_items():
    test_cart_page.open()

    test_cart_page.choice_item()

    test_cart_page.detail_item()

    test_cart_page.should_item('В корзине 1 шт')


def test_delete_cart_items():

    test_cart_page.open()

    test_cart_page.choice_item()

    test_cart_page.added_cart()

    test_cart_page.entrance_cart()

    #test_cart_page.delete_item()

    test_cart_page.should_cart('Ваша корзина пуста')


