from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

try: 
    link = "https://stepik.org/lesson/236895/step/1"
    browser = webdriver.Chrome()
    browser.get(link)
    
    time.sleep(3)
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.ID, 'ember33')
    input1.click()
    # перехидим на окно формы логин
  
    # вводим логин
    input_login =browser.find_element(By.CSS_SELECTOR, '[name="login"]')
    input_login.send_keys('')
    # вводим пароль
    input_passw = browser.find_element(By.ID, 'id_login_password')
    input_passw.send_keys('')
    # нажимаем на кнопку
    button_login = browser.find_element(By.CLASS, 'sign-form__btn.button_with-loader')  
    button_login.click()
   # browser.execute_script("return arguments[0].scrollIntoView(true);", BaseException)
      
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()