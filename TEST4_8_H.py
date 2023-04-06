from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x, y):
  return x + y
link = " https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    input2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    n1 = input1.text #берем текст из первого элемента
    n2 = input2.text #берем текст из второго элемента
    # считаем сумму
    s_12 = int(n1) + int(n2)
    
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    l = str(s_12)
    select.select_by_value(l) # ищем элемент с текстом суммы
   
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
