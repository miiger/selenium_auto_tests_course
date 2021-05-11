from selenium import webdriver
from time import sleep
import time

try:


        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        first_name = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input")
        first_name.send_keys("Abl")
        last_name = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
        last_name.send_keys("Abl")
        city = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
        city.send_keys("Abl")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()


        time.sleep(1)

    
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        
        welcome_text = welcome_text_elt.text


        assert "Congratulations! You have successfully registered!" == welcome_text

finally:


        time.sleep(10)
        browser.quit()




