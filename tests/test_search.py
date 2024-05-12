from boroda_land_project_tests.pages.search_page import search_page


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
