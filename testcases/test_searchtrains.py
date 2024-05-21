import time
from lib2to3.pgen2 import driver
from pageobjects.searchtrains import search_train
from selenium import webdriver
from utilities.Logger import LogGenerator

class Test_Search:
    log=LogGenerator.logen()

    def test_title01(self,setup):
         self.log.info("TestCase test_titel01 Started ")
         self.driver=setup

         if self.driver.title == "IRCTC Next Generation eTicketing System":
             time.sleep(3)
             self.driver.save_screenshot("D:\\IRCTC\\Screenshots\\test_titel01pass.png")
             assert True
             self.log.info("TestCase test_titel01 Pass ")
         else:
             time.sleep(3)
             self.driver.save_screenshot("D:\\IRCTC\\Screenshots\\test_titel01fail.png")
             self.log.info("TestCase test_titel01 fail ")
             assert False

    def test_trainsearch(self,setup):
         self.driver=setup
         self.search=search_train(self.driver)
         self.search.Enter_From("PUNE JN - PUNE (PUNE)")
         self.log.info("From City")
         self.search.Enter_To("NASHIK ROAD - NK (NASHIK)")
         self.log.info("To City")
         self.search.Date_Pick()
         self.log.info("date selected ")
         self.search.Class_Option()
         self.log.info("Class option filled")
         self.search.Search_Button()
         time.sleep(3)




