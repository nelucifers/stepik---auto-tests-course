from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    element_num1 = browser.find_element_by_id("num1")
    num1 = int(element_num1.text)
    element_num2 = browser.find_element_by_id("num2")
    num2 = int(element_num2.text)
    sum = num1 + num2
    
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(str(sum))
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
	
finally:
	time.sleep(10)
	browser.quit()

