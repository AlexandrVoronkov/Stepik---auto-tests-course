from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element_by_css_selector(".btn")
    button1.click()
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
    time.sleep(1)
    x1 = browser.find_element_by_css_selector("#input_value")
    x2 = x1.text
    x3 = calc(x2)
    anw1 = browser.find_element_by_css_selector("#answer")
    anw1.send_keys(x3)
    button = browser.find_element_by_tag_name("button")
    button.click()
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()