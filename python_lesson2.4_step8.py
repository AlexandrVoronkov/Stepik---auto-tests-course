from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
txt1 = WebDriverWait(browser, 12).until(
     EC.text_to_be_present_in_element((By.ID, "price"), "$100")
 )
button = browser.find_element_by_id("book")
button.click()
x_1 = browser.find_element_by_css_selector("#input_value")
x_2 = x_1.text
f_x = calc(x_2)
answer = browser.find_element_by_css_selector("#answer")
answer.send_keys(f_x)
button2 = browser.find_element_by_id("solve")
button2.click()
