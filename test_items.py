import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_cart_button_presence(browser):
    browser.get(link)
    time.sleep(10)
    try:
        button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    except NoSuchElementException:
        button = None
    assert button is not None, "No 'Add to cart' button on this page."
