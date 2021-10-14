from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_name = browser.find_element_by_css_selector('#input_value')
    x = x_name.text
    y = calc(x)
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)
    robotCheckbox = browser.find_element_by_css_selector('#robotCheckbox')
    robotCheckbox.click()
    robotsRule = browser.find_element_by_css_selector('#robotsRule')
    robotsRule.click()
    time.sleep(4)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn").click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()