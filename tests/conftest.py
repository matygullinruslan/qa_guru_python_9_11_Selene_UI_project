import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from utils import attach
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
remote_browser_url = os.getenv('REMOTE_BROWSER_URL')


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser.config.base_url = 'https://boroda.land'
    browser.config.window_width = 1900
    browser.config.window_height = 1080

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{remote_browser_url}",
        options=options)

    browser.config.driver = driver
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()



# @pytest.fixture(scope='function', autouse=True)
#
# def setup_browser(request):
#
#     browser.config.base_url = 'https://boroda.land'
#     browser.config.window_width = 1900
#     browser.config.window_height = 1080
#     driver_options = webdriver.ChromeOptions()
#     driver_options.page_load_strategy = 'eager'
#     browser.config.driver_options = driver_options
#     yield browser
#     browser.quit()