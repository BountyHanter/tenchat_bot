from selenium import webdriver
import time
import auth_info
from confirm_code.confirm_code import show_message
from auth_info import login, password
import os
from fake_useragent import UserAgent
# Подключение прокси - https://www.youtube.com/watch?v=sZcs5eNT4Cc&list=PLqGS6O1-DZLp1kgiQNpueIMCHRNzgHa1r

# Добавляем юзер агент
useragent = UserAgent()

# Четко показываем расположение вебдрайвера
install_dir = "/snap/firefox/current/usr/lib/firefox"
driver_loc = os.path.join(install_dir, "geckodriver")
binary_loc = os.path.join(install_dir, "firefox")

service = webdriver.FirefoxService(driver_loc)
opts = webdriver.FirefoxOptions()
opts.binary_location = binary_loc
# Устанавливаем юзер агент
opts.set_preference("general.useragent.override", useragent.random)
driver = webdriver.Firefox(service=service, options=opts)

url = "https://vk.com/"


try:
    driver.get(url=url)
    email_input = driver.find_element(by='id', value='index_email')
    email_input.clear()
    email_input.send_keys(login)

    driver.find_element(by='class name', value='VkIdForm__signInButton').click()

    conf_code = show_message()
    confirm_code_input = driver.find_element(by='class name', value='vkc__TextField__codeInput')
    confirm_code_input.clear()
    confirm_code_input.send_keys(conf_code)
    driver.find_element(by='class name', value='vkuiButton__in').click()

    pswd = driver.find_element(by='name', value='password')
    pswd.clear()
    pswd.send_keys(password)
    driver.find_element(by='class name', value='vkuiButton__in').click()
    time.sleep(100)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
