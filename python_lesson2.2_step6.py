import math
import time
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_1 = browser.find_element_by_css_selector("#input_value")
    x_2 = x_1.text
    f_x = calc(x_2)
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(f_x)
    robotCheckbox = browser.find_element_by_css_selector('#robotCheckbox')
    robotCheckbox.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotCheckbox)
    robotsRule = browser.find_element_by_css_selector('#robotsRule')
    robotsRule.click()
    time.sleep(1)
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()