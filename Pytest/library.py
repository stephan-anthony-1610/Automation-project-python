class wapper:
    def __init__(self,driver):
        self.driver=driver
    def click(self,locator):
        self.driver.find_element(*locator).click()
    def enter(self,locator,data):
        self.driver.find_element(*locator).send_keys(data)
