import pytest
from selenium.webdriver.common.by import By

class Test_dif_language:
    def test_find_basket(self, browser):
        browser.implicitly_wait(10)
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        assert browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-baske'), 'Add to basket button is not found'

if __name__ == "__main__":
    pytest.main()