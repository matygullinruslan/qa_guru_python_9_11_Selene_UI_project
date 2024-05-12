from boroda_land_project_tests.pages.favorites_page import favorites_page
import pytest


@pytest.mark.xfail(reason='После добавления товара в избранное он не отображается на вкладке "Избранное"')
def test_added_cart_favorites():

    favorites_page.open()

    favorites_page.find_cart('Поясная сумка')
    favorites_page.detail_item()
    favorites_page.add_to_favorites()
    favorites_page.entrance_to_favorites()

    favorites_page.should_to_favorites('BAG379-3 Мужская поясная сумка ручной работы их натуральной кожи')
