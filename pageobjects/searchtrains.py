import time

import pytest
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class search_train:
    Text_From_XP=(By.XPATH,"//input[@class='ng-tns-c57-8 ui-inputtext ui-widget ui-state-default ui-corner-all ui-autocomplete-input ng-star-inserted']")
    Text_To_XP=(By.XPATH,"//input[@class='ng-tns-c57-9 ui-inputtext ui-widget ui-state-default ui-corner-all ui-autocomplete-input ng-star-inserted']")
    DatePicker_XP = (By.XPATH, "//*[@id='jDate']")
    Class_Select_XP = (By.XPATH, "//span[@class='ui-dropdown-trigger-icon ui-clickable ng-tns-c65-11 pi pi-chevron-down']")
    Click_Search_XP = (By.XPATH, "//button[@type='submit']")


    def __init__(self,driver):
        self.driver=driver
        self.wait= WebDriverWait(self.driver,10)




    def Enter_From(self,From):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_From_XP))
        self.driver.find_element(*search_train.Text_From_XP).send_keys(From)
        self.driver.find_element(*search_train.Text_From_XP).send_keys(Keys.TAB)


    def Enter_To(self,To):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_To_XP))
        self.driver.find_element(*search_train.Text_To_XP).send_keys(To)
        self.driver.find_element(*search_train.Text_To_XP).send_keys(Keys.TAB)


    def Date_Pick(self):
        self.driver.find_element(*search_train.DatePicker_XP).click()
        self.wait.until(expected_conditions.visibility_of_element_located(self.DatePicker_XP))
        Date=self.driver.find_element(By.XPATH,"//a[normalize-space()='24']")
        Date.click()
        time.sleep(3)



    def Class_Option(self):
        action = ActionChains(self.driver)
        self.wait.until(expected_conditions.visibility_of_element_located(self.Class_Select_XP))
        action.move_to_element(self.driver.find_element(*search_train.Class_Select_XP)).click().perform()
        self.wait.until(expected_conditions.visibility_of_element_located(self.Class_Select_XP))
        Sleeper = self.driver.find_element(By.XPATH,"//span[@class='ng-star-inserted'][normalize-space()='Sleeper (SL)']")
        Sleeper.click()


    def Search_Button(self):
        self.driver.find_element(*search_train.Click_Search_XP).click()







