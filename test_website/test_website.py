from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

try: 
    link = "https://zdravmir.github.io/"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, '[href="#description"]')
    input1.click()
   # B = browser.find_element(By.TAG_NAME, "button")
   # browser.execute_script("return arguments[0].scrollIntoView(true);", BaseException)
      
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()