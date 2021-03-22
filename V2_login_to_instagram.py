from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import instagram_username, instagram_password

import time

CHROME_DRIVER_PATH = "C:\Chromedriver\chromedriver.exe"
instagram_username = instagram_username
instagram_password = instagram_password

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)


def login():
    try:
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = driver.find_element_by_name("username")
        username.clear()
        username.send_keys(instagram_username)
        time.sleep(2)

        password = driver.find_element_by_name("password")
        password.clear()
        password.send_keys(instagram_password)
        time.sleep(2)

        password.send_keys(Keys.ENTER)
        time.sleep(20)

        driver.close()
        driver.quit()

    except Exception as ex:
        print(ex)
        driver.close()
        driver.quit()


login()