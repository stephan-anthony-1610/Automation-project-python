from library import *
from Excell import *
file=r"/home/st3ph4n/Documents/POM.xlsx"
class Home:
    # locator={"login":("xpath","//a[text()='Log in']"),
    #          "register":("xpath","//a[text()='Register']")}
    locator=read_locator(file,"HomePage1")
    def __init__(self,driver):
        self.driver=driver
    def login(self):
        log=wapper(self.driver)
        log.click(self.locator["login"])
    def register(self):
        reg=wapper(self.driver)
        reg.click(self.locator["register"])