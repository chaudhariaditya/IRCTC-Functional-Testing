from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Select_Train:
    Click_Option_XP=(By.XPATH,"//td[1]//div[1]//div[1]")
    Click_Add_Option_Xp=(By.XPATH,"//body/app-root/app-home[@class='ng-star-inserted']/div[@id='divMain']/div/app-train-list[@class='ng-star-inserted']/div[@class='col-sm-9 col-xs-12']/div[@class='tbis-div']/div[@class='ng-star-inserted']/div[@class='ng-star-inserted']/div[@class='form-group no-pad col-xs-12 bull-back border-all']/app-train-avl-enq/div[@class='ng-star-inserted']/div[@class='dull-back no-pad col-xs-12']/div[@class='col-xs-12 ng-star-inserted']/div[@class='ng-star-inserted']/table/tr/td[2]/div[1]")
    Click_Book_Now_Xp=(By.XPATH,"//button[@type='submit']")



    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)



    def Option_Click(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_Option_XP))
        self.driver.find_element(*Select_Train.Click_Option_XP).click()
    def Add_Option(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_Add_Option_Xp))
        self.driver.find_element(*Select_Train.Click_Add_Option_Xp).click()



    def Click_Book(self):

        self.driver.find_element(*Select_Train.Click_Book_Now_Xp).click()
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_Book_Now_Xp))


