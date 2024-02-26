from selene import browser, have, be, by

def test_search_items():
    browser.open('/')
    browser.element(by.name('q')).should(be.blank).type('Кожаная дорожная сумка').press_enter()
    browser.element('.product-preview__title').should(have.text('BAG521-1 Кожаная дорожная сумка с ручками и ремнем'))

def test_search_by_articles():
    browser.open('/')
    browser.element(by.name('q')).should(be.blank).type('RAZ1035').press_enter()
    browser.element('.product-preview__title').should(have.text('RAZ1035 Гель для бритья EMERALD от Barbaro (200 мл)'))
    ...

def test_incorrect_search():
    browser.open('/')
    browser.element(by.name('q')).should(be.blank).type('rj;fyst rhnrb').press_enter()
    browser.element('.empty-catalog-message').should(have.text('По вашему запросу ничего не найдено'))


#добавление товара в корзину, удаление товара из корзины. Добавление товара в избранное, удаление товара из избранного.