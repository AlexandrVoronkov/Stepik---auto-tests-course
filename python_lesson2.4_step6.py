from selenium import webdriver

browser = webdriver.Chrome()
try:
# говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/cats.html")
    browser.find_element_by_id("button")
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта

    # закрываем браузер после всех манипуляций
    browser.quit()