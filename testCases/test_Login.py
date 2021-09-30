import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = Readconfig.getApplicationURL()
    Username = Readconfig.getUseremail()
    Password = Readconfig.getPassword()

    logger=LogGen.loggen()

    def test_homepageTitle(self, setup):
        self.logger.info("*************Test 001**************")
        self.logger.info("**********started*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            time.sleep(10)
            assert True
            self.driver.close()
            self.logger.info("****************Passed****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            self.driver.close()
            self.logger.error("************Fail**********************")
            assert False


    def test_Login(self, setup):
        self.logger.info("****************Verifying Login test****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.Username)
        self.lp.setPassword(self.Password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("****************Passed****************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("****************Failed****************")
            assert False
