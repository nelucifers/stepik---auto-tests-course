# The owls are not what they seem! OvO

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time
import math

@pytest.mark.parametrize('id_lesson', ["236895" ,"236896" ,"236897" ,"236898" ,"236899" ,"236903" ,"236904" ,"236905"])
def test_guest_should_see_login_link(id_lesson):
    try:
        link = f"https://stepik.org/lesson/{id_lesson}/step/1"
        browser = webdriver.Chrome()
        browser.get(link)
        answer = str(math.log(int(time.time())))
        textarea = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea.textarea"))
        )
        textarea.send_keys(answer)
        button = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button.submit-submission"))
        )
        button.click()
	
        result = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint"))
        )
        text = result.text
        assert text == "Correct!", text
    finally:
        browser.quit()
