from page.favorites_page import favorites_page


def test_added_cart_favorites():

    favorites_page.open()

    favorites_page.find_cart('Поясная сумка')

    favorites_page.detail_item()

    favorites_page.add_to_favorites()

    favorites_page.entrance_to_favorites()

    favorites_page.should_to_favorites('BAG379-3 Мужская поясная сумка ручной работы их натуральной кожи')
# #тест не проходит из-за баги,
# # после добавления товара в избранное он не отображается на вкладке "Избранное"


# def test_added_page_favorites():
#     browser.open('/')
#     browser.element(by.name('q')).should(be.blank).type('Поясная сумка').press_enter()
#     browser.element('.product-preview__title').click()
#     browser.element('.icon-favorites-o').click()
#     browser.element('[href="/page/favorites"]').click()
#     browser.element('.static-text').should(have.text(
#             'BAG379-3 Мужская поясная сумка ручной работы из натуральной кожи'))
#
# #тест не проходит из-за баги,
# # после добавления товара в избранное он не отображается на вкладке "Избранное"
