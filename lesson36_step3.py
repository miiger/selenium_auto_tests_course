from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import pytest

@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('url', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_stepik_link(browser, url):
    answer = math.log(int(time.time()))
    link = f"https://stepik.org/lesson/236{url}/step/1"
    browser.implicitly_wait(10)
    browser.get(link)

    input1 = browser.find_element_by_class_name("string-quiz__textarea")
    input1.send_keys(str(answer))
       
    button = browser.find_element_by_class_name("submit-submission")
    button.click()

    feedback = browser.find_element_by_class_name("smart-hints__hint").text
    
    print(browser.find_element_by_class_name("smart-hints__hint").text)
    assert feedback == "Correct!"
    

    
