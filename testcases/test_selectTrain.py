import time

from pageobjects.Selecttrain import Select_Train
from pageobjects.searchtrains import search_train
from utilities.Logger import LogGenerator

class Test_Select_Train:
    log = LogGenerator.logen()

    def test_add(self,setup):
        self.driver = setup
        self.search = search_train(self.driver)
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
        self.log.info("trains")

        self.click=Select_Train(self.driver)
        self.click.Option_Click()
        self.log.info("Select option")
        self.click.Add_Option()
        self.log.info("Add option")
        self.click.Click_Book()
        self.log.info("Book train")

