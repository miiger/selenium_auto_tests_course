from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time



try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_id("num1").text
    y_element = browser.find_element_by_id("num2").text

    sum = int(x_element) + int(y_element)
    

    select = Select(browser.find_element_by_css_selector(".custom-select"))
    select.select_by_value(str(sum))

    
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
