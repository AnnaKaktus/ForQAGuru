from selene.support.shared import browser
from selene import be, have
import pytest

@pytest.fixture
def set_browser():
    browser.config.window_width = 1000
    browser.config.window_height = 800
    yield
    browser.quit()

def test_search_selene(set_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_ghoijgogokgop(set_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('ghoijgogokgo').press_enter()
    browser.element('[class="card-section"]').should(have.text('ничего не найдено'))
