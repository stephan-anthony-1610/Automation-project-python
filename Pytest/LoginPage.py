from library import *
from Excell import *
file=r"/home/st3ph4n/Documents/POM.xlsx"
class Login:
    # locator={"Email":("id","Email"),
    #          "Password":("id","Password"),
    #          "Log in":("xpath","//input[@value='Log in']")}
    locator=read_locator(file,"LoginPage1")
    def __init__(self,driver):
        self.driver=driver
    def login(self,email,password):
        obj1=wapper(self.driver)
        obj1.enter(self.locator["Email"],email)
        obj1.enter(self.locator["Password"],password)
        obj1.click(self.locator["Log in"])
