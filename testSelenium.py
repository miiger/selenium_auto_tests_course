from selenium import webdriver
from time import sleep
import math

url="http://suninjuly.github.io/registration1.html"


browser=webdriver.Chrome()
browser.get(url)
input1=browser.find_element_by_css_selector(".first[required]")
input1.send_keys("NAME")
input2=browser.find_element_by_css_selector(".second[required]")
input2.send_keys("LASTNAME")
input3=browser.find_element_by_css_selector(".third[required]")
input3.send_keys("EMAIL")
sleep(1)
button=browser.find_element_by_css_selector("button")
button.click()

text=browser.find_element_by_css_selector("h1")
assert text.text=="Congratulations! You have successfully registered!"




