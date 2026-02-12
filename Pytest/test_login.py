from HomePage import *
from LoginPage import *
import pytest

data=[("stephan@gmail.com","St3ph4n_xd"),("bharath@gmail.com","bharath@1234"),("aadhitiya@gmail.com","aadhitiya@1234")]
@pytest.mark.parametrize("email,password",data)
def test_log(_driver,email,password):
    driver=_driver
    obj3=Home(driver)
    obj3.login()
    obj4=Login(driver)
    obj4.login(email,password)
