from library import *
from Excell import *
file=r"/home/st3ph4n/Documents/POM.xlsx"
class Register:
    # locator={"Male":("id","gender-male"),
    #          "Female":("id","gender-female"),
    #          "Fname":("id","FirstName"),
    #          "Lname":("id","LastName"),
    #          "Email":("id","Email"),
    #          "Password":("id","Password"),
    #          "ConfirmPassword":("id","ConfirmPassword")}
    locator=read_locator(file,"RegisterPage1")
    def __init__(self,driver):
        self.driver=driver
    def register(self,gender,fname,lname,email,password,confirmpassword):
        obj2=wapper(self.driver)
        if gender.lower()=="male":
            obj2.click(self.locator["Male"])
        else:
            obj2.click(self.locator["Female"])
        obj2.enter(self.locator["Fname"],fname)
        obj2.enter(self.locator["Lname"],lname)
        obj2.enter(self.locator["Email"],email)
        obj2.enter(self.locator["Password"],password)
        obj2.enter(self.locator["ConfirmPassword"],confirmpassword)