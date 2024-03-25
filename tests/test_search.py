import allure
from page.search_page import search_page


def test_search_item():
    search_page.open()

    search_page.search_item('Кожаная дорожная сумка')

    search_page.should_item('BAG521-1 Кожаная дорожная сумка с ручками и ремнем')


def test_search_by_articles():
    search_page.open()

    search_page.search_item('RAZ1035')

    search_page.should_articles('RAZ1035 Гель для бритья EMERALD от Barbaro (200 мл)')


def test_incorrect_search():
    search_page.open()

    search_page.search_item('rj;fyst rhnrb')

    search_page.should_incorrect_search('По вашему запросу ничего не найдено')

# def test_search_items():
#     browser.open('/')
#     browser.element(by.name('q')).should(be.blank).type('Кожаная дорожная сумка').press_enter()
#     browser.element('.product-preview__title').should(have.text('BAG521-1 Кожаная дорожная сумка с ручками и ремнем'))
#
#
# def test_search_by_articles():
#     browser.open('/')
#     browser.element(by.name('q')).should(be.blank).type('RAZ1035').press_enter()
#     browser.element('.product-preview__title').should(have.text('RAZ1035 Гель для бритья EMERALD от Barbaro (200 мл)'))
#
#
# def test_incorrect_search():
#     browser.open('/')
#     browser.element(by.name('q')).should(be.blank).type('rj;fyst rhnrb').press_enter()
#     browser.element('.empty-catalog-message').should(have.text('По вашему запросу ничего не найдено'))
