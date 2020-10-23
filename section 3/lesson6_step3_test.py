from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time
import math

# @pytest.mark.parametrize('id_lesson', ["236895" ,"236896" ,"236897" ,"236898" ,"236899" ,"236903" ,"236904" ,"236905"])

try:
    link = "https://stepik.org/lesson/236895/step/1"
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
    time.sleep(1)
    browser.quit()
