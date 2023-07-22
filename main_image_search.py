from typing import Self
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
import time
# import include_image_search


# class selenium.webdriver.common. alert Alert(driver)
# sa.print1 (self)


class functions:
    def __init__(self, driver, switch_to, find_element):
        self.driver = driver
        self.switch_to = switch_to
        self.find_element = find_element

    def automation(self, message):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")
        driver.maximize_window()
        # include_image_search.mouse_movement(self)

        driver.switch_to.frame("callout")
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//button[@aria-label='Stay signed out']").click()
        time.sleep(3)
        driver.switch_to.parent_frame()

        time.sleep(3)

        driver.find_element(
            By.XPATH, "//g-flat-button[@jsname='ZnuYW']").send_keys(Keys.ENTER)

        # action.move_to_element(firstLevelMenu).perform()
        # time.sleep(3)
        # secondLevelMenu = driver.find_element(
        #     By.XPATH, "//a[@aria-label='Google apps']")
        # action.move_to_element(secondLevelMenu).perform()
        # time.sleep(3)

        # include_image_search.mouse_movement(Self)
        # functions.mouse_movement(self)
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element(By.ID, "APjFqb")
        action.move_to_element(firstLevelMenu).perform()
        time.sleep(3)
        secondLevelMenu = driver.find_element(
            By.XPATH, "//a[@aria-label='Google apps']")
        action.move_to_element(secondLevelMenu).perform()
        time.sleep(3)

        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located(
                (By.XPATH, "//a[@aria-label='Search for Images (opens a new tab)']"))).click()

        except:
            print(" ---------------invalid path -----------------")

        image = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")

        image.send_keys(message)

        e = driver.find_element(
            By.XPATH, "//span[@class='z1asCe MZy1Rb']//*[name()='svg']")

        e.click()
        driver.execute_script("window.scrollBy(0,5000)", "")
        time.sleep(5)

    def delete_pop_up(self):
        print("================================================================")
        self.driver.switch_to.frame("callout")
        time.sleep(3)
        self.driverfind_element(
            By.XPATH, "//button[@aria-label='No thanks']").click()
        time.sleep(3)

    def mouse_movement(self):
        print("================================================================")
        action = ActionChains(self.driver)
        firstLevelMenu = driver.find_element(By.ID, "APjFqb")
        action.move_to_element(firstLevelMenu).perform()
        time.sleep(3)
        secondLevelMenu = driver.find_element(
            By.XPATH, "//a[@aria-label='Google apps']")
        action.move_to_element(secondLevelMenu).perform()
        time.sleep(3)


# input_intake = input("Enter the image name need to be searched  ")
# automation(Self, input_intake)
