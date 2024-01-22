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

url_auth = 'https://tenchat.ru'

try:
    driver.get(url_auth)
    time.sleep(2)

    with open('coockies.json', 'r') as f:
        cookies = json.load(f)

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()
    time.sleep(5)
    driver.get('https://tenchat.ru/editor')
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
