from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.parametrize("min_popularity", [10**7, 1.5*10**7, 5*10**7, 10**8, 5*10**8, 10**9, 1.5*10**9])
def test_website_popularity(min_popularity):
    try: 
        link = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(10)
        errors = []
        
        x_elements = browser.find_elements(By.CSS_SELECTOR, "table:nth-of-type(1) tbody td:nth-child(2)")
        num_elements = [x.text for x in x_elements]
        #print(num_elements)
        
        for num_element in num_elements:
            #assert num_element >= min_popularity, f"website has {num_element} unique visitors per month. (Expected more than {min_popularity})"
            if num_element < min_popularity:
                errors.append(f"website has {num_element} unique visitors per month. (Expected more than {min_popularity})")
        assert not errors, "".join(errors)
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

