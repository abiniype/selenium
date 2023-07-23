from typing import Self
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
import time
from main_image_search import functions

# def delete_pop_up(self):
#     print("================================================================")
#     self.self.driver = webself.driver.Chrome()
#     time.sleep(3)
#     self.driver.switch_to.frame("callout")
#     self.self.driverfind_element(
#         By.XPATH, "//button[@aria-label='No thanks']").click()
#     time.sleep(3)
#     self.driver.switch_to.parent_frame()


# def mouse_movement(self):
#     print("================================================================")
#     action = ActionChains(self.driver)
#     firstLevelMenu = self.driver.find_element(By.ID, "APjFqb")
#     action.move_to_element(firstLevelMenu).perform()
#     time.sleep(3)
#     secondLevelMenu = self.driver.find_element(
#         By.XPATH, "//a[@aria-label='Google apps']")
#     action.move_to_element(secondLevelMenu).perform()
#     time.sleep(3)

input_intake = input("Enter the image name need to be searched  ")
functions.automation(Self, input_intake,"https://www.google.com")
