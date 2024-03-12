from selene import browser, have, be, by


class Searchpage:

    def open(self):
        browser.open('/')

    def search_item(self, item):
        browser.element(by.name('q')).should(be.blank).type(item).press_enter()

    def should_item(self, bag):
        browser.element('.product-preview__title').should(
            have.text(bag))

    def should_articles(self, articles):
        browser.element('.product-preview__title').should(
            have.text(articles))

    def should_incorrect_search(self, text):
        browser.element('.empty-catalog-message').should(have.text(text))


search_page = Searchpage

#     def test_search_items():
#         browser.open('/')
#         browser.element(by.name('q')).should(be.blank).type('Кожаная дорожная сумка').press_enter()
#         browser.element('.product-preview__title').should(
#             have.text('BAG521-1 Кожаная дорожная сумка с ручками и ремнем'))
#
#     def test_search_by_articles():
#         browser.open('/')
#         browser.element(by.name('q')).should(be.blank).type('RAZ1035').press_enter()
#         browser.element('.product-preview__title').should(
#             have.text('RAZ1035 Гель для бритья EMERALD от Barbaro (200 мл)'))
#
#     def test_incorrect_search():
#         browser.open('/')
#         browser.element(by.name('q')).should(be.blank).type('rj;fyst rhnrb').press_enter()
#         browser.element('.empty-catalog-message').should(have.text('По вашему запросу ничего не найдено'))
