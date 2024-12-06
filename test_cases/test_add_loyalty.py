import pytest
import time
import random
import string
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Add_Loyalty import Add_Loyalty_Page


def generate_random_code(self):
    letters = string.ascii_letters
    random_code = ''.join(random.choice(letters) for _ in range(self))
    return random_code


class TestAddNewLoyalty:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()

    def test_add_new_Loyalty(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Loyalty = Add_Loyalty_Page(self.driver)
        self.add_Loyalty.click_setting()
        self.add_Loyalty.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Loyalty.hover_Dis(hold_time=5)
        self.add_Loyalty.hover_Setup(hold_time=5)
        self.add_Loyalty.click_Loyalty()
        time.sleep(5)
        self.add_Loyalty.click_Loyalty_Add_Button()
        time.sleep(2)

        # Generate a random name for the Loyalty code
        self.random_code = generate_random_code(6)
        self.add_Loyalty.enter_Loyalty_code(self.random_code)
        self.add_Loyalty.enter_Loyalty_From("1")
        self.add_Loyalty.enter_Loyalty_To("2")
        self.add_Loyalty.click_Loyalty_save()
        time.sleep(5)

        Loyalty_add_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Loyalty code added successfully')]")))
        act_saved_text = Loyalty_add_success_msg.text
        exp_saved_text = "Loyalty code added successfully"
        if act_saved_text == exp_saved_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_add_new_Loyalty.png")
            self.driver.close()
            assert False


    def test_update_new_Loyalty(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        time.sleep(10)

        self.add_Loyalty = Add_Loyalty_Page(self.driver)
        self.add_Loyalty.click_setting()
        self.add_Loyalty.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Loyalty.hover_Dis(hold_time=5)
        self.add_Loyalty.hover_Setup(hold_time=5)
        self.add_Loyalty.click_Loyalty()
        time.sleep(5)
        self.add_Loyalty.click_Loyalty_action_button()
        time.sleep(3)
        self.add_Loyalty.click_Loyalty_edit_info_button()
        time.sleep(3)
        self.add_Loyalty.enter_Loyalty_code("")
        time.sleep(3)
        self.add_Loyalty.click_Loyalty_update_button()
        time.sleep(5)

        Loyalty_update_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Loyalty code updated successfully')]")))
        act_saved_text = Loyalty_update_success_msg.text
        exp_saved_text = "Loyalty code updated successfully"
        if act_saved_text == exp_saved_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_update_new_Loyalty.png")
            self.driver.close()
            assert False


    def test_search_new_Loyalty(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Loyalty = Add_Loyalty_Page(self.driver)
        self.add_Loyalty.click_setting()
        self.add_Loyalty.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Loyalty.hover_Dis(hold_time=5)
        self.add_Loyalty.hover_Setup(hold_time=5)
        self.add_Loyalty.click_Loyalty()
        time.sleep(5)
        self.add_Loyalty.click_Loyalty_code_search_button()
        time.sleep(3)
        self.add_Loyalty.enter_Loyalty_code_searchbar("Fresher")
        Loyalty_search_code = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(
            (By.XPATH, "//mat-cell[@data-label='LoyaltyCode' and contains(text(), 'Fresher')]")))
        act_Loyalty_search = Loyalty_search_code.text
        exp_Loyalty_search = "Fresher"
        if act_Loyalty_search == exp_Loyalty_search:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_search_new_Loyalty.png")
            self.driver.close()
            assert False


    def test_delete_new_Loyalty(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Loyalty = Add_Loyalty_Page(self.driver)
        self.add_Loyalty.click_setting()
        self.add_Loyalty.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Loyalty.hover_Dis(hold_time=5)
        self.add_Loyalty.hover_Setup(hold_time=5)
        self.add_Loyalty.click_Loyalty()
        time.sleep(10)
        self.add_Loyalty.click_Loyalty_action_button()
        time.sleep(10)
        self.add_Loyalty.click_Loyalty_code_delete()
        time.sleep(10)
        self.add_Loyalty.click_Loyalty_code_inactive()
        time.sleep(5)

        Loyalty_delete_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Status updated Successfully.')]")))
        act_delete_text = Loyalty_delete_success_msg.text
        exp_delete_text = "Status updated Successfully."
        if act_delete_text == exp_delete_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_delete_new_Loyalty.png")
            self.driver.close()
            assert False


    def test_active_new_Loyalty(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Loyalty = Add_Loyalty_Page(self.driver)
        self.add_Loyalty.click_setting()
        self.add_Loyalty.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Loyalty.hover_Dis(hold_time=5)
        self.add_Loyalty.hover_Setup(hold_time=5)
        self.add_Loyalty.click_Loyalty()
        time.sleep(10)
        self.add_Loyalty.click_Loyalty_action_button()
        time.sleep(10)
        self.add_Loyalty.click_Loyalty_code_active()
        time.sleep(10)
        self.add_Loyalty.click_Loyalty_code_active_button()
        time.sleep(5)

        Loyalty_active_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Status updated Successfully.')]")))
        act_active_text = Loyalty_active_success_msg.text
        exp_active_text = "Status updated Successfully."
        if act_active_text == exp_active_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_active_new_Loyalty.png")
            self.driver.close()
            assert False
