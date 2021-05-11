from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math



try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    #browser.implicitly_wait(5)
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element(
        (By.ID, "price"), "100"))

    browser.find_element_by_id("book").click()                                         

    x = browser.find_element_by_id("input_value").text
    
    result = math.log(abs(12*math.sin(int(x))))

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(result))
       
    # Отправляем заполненную форму
    button = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
