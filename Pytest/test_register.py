from HomePage import *
from RegisterPage import *
import pytest

data=[("Male","Stephan","Anthony","stephan@gmail.com","St3ph4n_xd","st3ph4n_xd"),
      ("Male","Aadhitiya","Bharath","aadhitiya@gmail.com","aadhitiya@134","aadhitiya@134"),
      ("Male","Bharath","likith","bharath@gmail.com","bharath@liki","bharath@liki")]
@pytest.mark.parametrize("gender,fname,lname,email,password,confirmpassword",data)
def test_reg(_driver,gender,fname,lname,email,password,confirmpassword):
    driver=_driver
    obj5=Home(driver)
    obj5.register()
    obj6=Register(driver)
    obj6.register(gender,fname,lname,email,password,confirmpassword)
