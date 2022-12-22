import string
import time

import requests
import selenium.common.exceptions
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://hh.ru/'
driver = webdriver.Chrome()
driver.get(url)

time.sleep(1 / 4)

driver.find_element(by=By.CLASS_NAME, value='supernova-button').click()

while True:
    print('пройдите регистрацию самостоятельно чтобы не отдавать мне данные')
    if input() == 'готово' and 'hh.ru' in driver.current_url:
        driver.find_element(by=By.CLASS_NAME, value='supernova-logo-wrapper').click()
        driver.find_element(by=By.TAG_NAME, value='input').send_keys('Python developer', Keys.ENTER)
        break
    print(driver.current_url)


def sender():
    lst_click = driver.find_elements(by=By.CLASS_NAME, value='serp-item__title')

    pos_y = 0

    for i in lst_click:
        while True:
            try:
                i.click()
                print('Clicked')
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[-1])
                lst = driver.find_elements(by=By.LINK_TEXT, value='Смотреть отклик')
                if not len(lst) != 0:
                    driver.find_element(by=By.LINK_TEXT, value='Откликнуться').click()
                    print('Откликнуться')

                    time.sleep(1)
                else:
                    print('Смотреть отклик')

                time.sleep(1)

                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            except selenium.common.exceptions.ElementClickInterceptedException:
                print('вне зоны видимости')
                pos_y += 200

                driver.execute_script(f"window.scrollTo(0, {pos_y})")
            else:
                break
        time.sleep(1)

    print(len(lst_click))


while True:
    sender()
    driver.execute_script(f"window.scrollTo(0, 800)")
    if len(driver.find_elements(by=By.LINK_TEXT, value='дальше')) == 0:
        break
    driver.find_element(by=By.LINK_TEXT, value='дальше').click()

    time.sleep(1)

time.sleep(10)
