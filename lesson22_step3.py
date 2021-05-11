from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os



try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'cama.txt')

    # Ваш код, который заполняет обязательные поля

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("ta")
    
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("cha")

    input3 = browser.find_element_by_name("email")
    input3.send_keys("egi@egi.com")

    input4 = browser.find_element_by_name("file")
    input4.send_keys(file_path)
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
