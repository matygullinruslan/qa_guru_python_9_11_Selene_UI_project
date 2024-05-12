from selene import browser, have, be, by
import allure


class SearchPage:
    def open(self):
        with allure.step('Открываем сайт'):
            browser.open('/')

    def search_item(self, item):
        with allure.step('Вводим в поисковой строке товар'):
            browser.element(by.name('q')).should(be.blank).type(item).press_enter()

    def should_item(self, bag):
        with allure.step('Проверяем, что товар найден'):
            browser.element('.product-preview__title').should(
                have.text(bag))

    def should_articles(self, articles):
        with allure.step('Проверяем, что товар найден по артикулу'):
            browser.element('.product-preview__title').should(
                have.text(articles))

    def should_incorrect_search(self, text):
        with allure.step('Проверяем, что товар не найден'):
            browser.element('.empty-catalog-message').should(have.text(text))


search_page = SearchPage()
