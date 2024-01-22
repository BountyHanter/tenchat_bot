import json
import time, os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth_info import phone
from confirm_code.confirm_code import show_message

s = Service(executable_path='/home/denis/Desktop/Projects/work/tanchat_bot/tanchat_auth_google/chromedriver-linux64/chromedriver')
driver = webdriver.Chrome(service=s)

url_auth = 'https://tenchat.ru/auth/sign-in'

try:

    driver.get(url=url_auth)
    time.sleep(2)
    phone_input = driver.find_element(by='class name', value='outline-none')
    phone_input.clear()
    phone_input.send_keys(phone)
    time.sleep(1)

    driver.find_element(by='class name', value='tc-btn-filled').click()
    time.sleep(5)
    inputs = driver.find_element(By.CLASS_NAME, value='space-x-3').find_elements(By.CLASS_NAME, value='rounded-xl')
    code = show_message()
    for num, i in enumerate(inputs):
        i.click()
        i.send_keys(code[num])
    time.sleep(5)
    cookies = driver.get_cookies()
    with open('coockies.json', 'w') as f:
        json.dump(cookies, f)
    time.sleep(6)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
