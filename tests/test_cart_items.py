from selene import browser, have, be, by


def test_added_cart_items():
    browser.open('/')
    browser.element(by.name('q')).should(be.blank).type('Шампунь').press_enter()
    browser.element('[href="/product/raz1016-muzhskoy-shampun-dlya-normalnyh-i-zhirnyh-volos-220-ml"]').click()
    browser.element('#product-detail-buy-area').click()
    browser.element('.add-cart-counter__detail-text').should(have.text('В корзине 1 шт'))


def test_delete_cart_items():
    browser.open('/')
    #browser.element('[href="/collection/britie"]').click()
    browser.element('[href="/collection/britie"]').hover()
    browser.element('[href="/collection/britie-sredstva-dlya-britya"]').click()
    browser.element('[href="/product/care143-loson-posle-britya-proraso-sandal-sandal"]').click()
    browser.element('.add-cart-counter').click()
    browser.element('.header__control-text').click()
    #browser.element('.js-item-delete').click()
    browser.element('.text-center').should(have.text('Ваша корзина пуста'))
    ...


