from selene import browser, have, be, by


def test_added_page_favorites():
    browser.open('/')
    browser.element(by.name('q')).should(be.blank).type('Поясная сумка').press_enter()
    browser.element('.product-preview__title').click()
    browser.element('.icon-favorites-o').click()
    browser.element('[href="/page/favorites"]').click()
    browser.element('.static-text').should(
        browser.element(".static-text").should.have.text(
            'BAG379-3 Мужская поясная сумка ручной работы их натуральной кожи'))
