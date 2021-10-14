from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector('[name="firstname"]')
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_css_selector('[name="lastname"]')
    last_name.send_keys("Petrov")
    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys("email")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'fileee.txt')  # добавляем к этому пути имя файла
    element2 = browser.find_element_by_css_selector("#file")
    element2.send_keys(file_path)
    button = browser.find_element_by_tag_name("button")
    button.click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()