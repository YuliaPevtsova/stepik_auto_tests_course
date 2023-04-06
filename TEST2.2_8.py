from selenium import webdriver
from selenium.webdriver.common.by import By
import os

try:
    link = "http://suninjuly.github.io/file_input.html" 
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.TAG_NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "email")
    input3.send_keys("asdad@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']") 
    element.send_keys(file_path)
    # print(os.path.abspath(__file__))
    # print(os.path.abspath(os.path.dirname(__file__)))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()