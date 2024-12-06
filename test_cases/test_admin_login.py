import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config


class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    invalid_password = Read_Config.get_invalid_password()

    ## test case 1
    def test_title_verification(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "FRE8"
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.driver.close()
            assert False

    ## test case 2
    def test_valid_admin_login(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.close()

    ## Test case 3
    def test_invalid_username_login(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        act_error = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Username does not exist')]")))
        act_error_text = act_error.text
        exp_error = "Username does not exist"
        if act_error_text == exp_error:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_username_login.png")
            self.driver.close()
            assert False

    ##Test case 4
    def test_invalid_password_login(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.invalid_password)
        self.admin_lp.click_login()
        act_error = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Incorrect password')]")))
        act_error_text = act_error.text
        exp_error = "Incorrect password"
        if act_error_text == exp_error:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_password_login.png")
            self.driver.close()
            assert False
