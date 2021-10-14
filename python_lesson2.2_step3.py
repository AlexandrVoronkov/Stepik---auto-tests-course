from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_css_selector('#num1')
    x1 = num1.text
    num2 = browser.find_element_by_css_selector('#num2')
    x2 = num2.text
    x3 = str(int(x1) + int(x2))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(x3)
    #select.select_by_value(x3)    #или так
    button = browser.find_element_by_css_selector(".btn").click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()