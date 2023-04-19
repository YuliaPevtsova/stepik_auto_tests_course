from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

def test_form_login(FIO, email, Phone, Transfer, HowManyPeople, HowManyChild, ChildAge):
    try: 
        link = "file:///C:/YULi/stepik_auto_tests_course/forma.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.NAME, "FIO")
        input1.send_keys(FIO)
        input2 = browser.find_element(By.NAME, "email")
        input2.send_keys(email)
        input3 = browser.find_element(By.NAME, "Phone")
        input3.send_keys(Phone)
        select1 = Select(browser.find_element(By.NAME, "Transfer"))
        select1.select_by_value(Transfer)
        select2 = Select(browser.find_element(By.NAME, "HowManyPeople"))
        select2.select_by_value(HowManyPeople)
        select3 = Select(browser.find_element(By.NAME, "HowManyChild"))
        select3.select_by_value(HowManyChild)
        input4 = browser.find_element(By.NAME, "ChildAge")
        input4.send_keys(ChildAge)


        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

# сделать в цикле подставление данных  из таблицы xl
# @pytest.mark.parametrize('language', ["ru", "en-gb"])