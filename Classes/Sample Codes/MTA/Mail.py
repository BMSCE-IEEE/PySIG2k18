# Title: DBMS
# Author: K Nitesh Srivats
# Date: 01/06/2018

import os
from time import sleep
import pandas as pd
import keyboard
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class Mail:
    def __init__(self):
        self.username = "@gmail.com"
        self.password = ""
        self.todo = pd.read_excel(os.path.join(os.getcwd(), "Mail_todo.xlsx"))

    def tabs(self, driver, n):
        ActionChains(driver).send_keys(Keys.TAB*n).perform()
        sleep(0.1)

    def click(self, driver, identifier):
        try:
            element = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, identifier)))
            element = driver.find_element_by_xpath(identifier).click()
        except TimeoutException:
            element = driver.find_element_by_xpath(identifier).click()

    def tabfill(self, driver, string, n):
        ActionChains(driver).send_keys(Keys.TAB*n).perform()
        keyboard.write(str(string))
        sleep(0.2)

    def tabenter(self, driver, n):
        ActionChains(driver).send_keys(Keys.TAB * n).perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        sleep(0.2)

    def down(self, driver, n):
        ActionChains(driver).send_keys(Keys.ARROW_DOWN*n).perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        sleep(0.2)

    def wait(self, driver, identifier):
        element = WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, identifier)))

    def send_mail(self):
        subject = "Mail Test IEEE"
        file = open("Content.txt")
        done = pd.read_excel(os.path.join(os.getcwd(), "Join.xlsx"))
        done["Done"] = pd.Series()
        done.fillna("No", inplace=True)
        content = ""
        for i in file:
            content += i

        self.todo["Path"].iloc[1] = self.username
        self.todo["Path"].iloc[4] = self.password
        self.todo["Path"].iloc[15] = subject
        self.todo["Path"].iloc[19] = content

        exe_path = os.path.join(os.getcwd(), "chromedriver.exe")
        driver = webdriver.Chrome(executable_path=exe_path)
        driver.implicitly_wait(30)
        driver.get("https://www.google.com/intl/en-GB/gmail/about/#")
        driver.maximize_window()

        for i in range(len(self.todo)):
            task = self.todo["Task"].iloc[i]
            path = self.todo["Path"].iloc[i]
            if task == "Sleep":
                sleep(path)
            elif task == "Tab":
                self.tabs(driver, path)
            elif task == "Click":
                self.click(driver, path)
            elif task == "TabEnter":
                self.tabenter(driver, path)
            elif task == "Enter":
                ActionChains(driver).send_keys(Keys.RETURN).perform()
            elif task == "Email":
                for j in range(len(done)):
                    if done["Done"].iloc[j] != "Yes":
                        keyboard.write(done["Username"].iloc[j])
                        keyboard.write(" ")
                        done["Done"] = "Yes"
                        sleep(0.2)
            elif task == "Keyboard":
                keyboard.write(done["Path"].iloc[i])
                sleep(0.5)
            elif task == "BCC":
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('shift')
                pyautogui.keyDown('b')
                sleep(0.01)
                pyautogui.keyUp('ctrl')
                pyautogui.keyUp('shift')
                pyautogui.keyUp('b')

        done.to_excel("Sent_Mails.xlsx", index=False)

