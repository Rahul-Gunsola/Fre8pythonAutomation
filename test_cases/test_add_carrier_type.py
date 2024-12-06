import pytest
import time
import random
import string
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Add_Carrier_Type import Add_Carrier_Type_Page


def generate_random_name(self):
    letters = string.ascii_letters
    random_name = ''.join(random.choice(letters) for _ in range(self))
    return random_name


class TestAddNewCarrierType:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()


    def test_add_new_Carrier_Type(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Carrier_Type = Add_Carrier_Type_Page(self.driver)
        self.add_Carrier_Type.click_setting()
        self.add_Carrier_Type.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Carrier_Type.hover_Dis(hold_time=5)
        self.add_Carrier_Type.hover_Setup(hold_time=5)
        self.add_Carrier_Type.click_Carrier_Type()
        time.sleep(5)
        self.add_Carrier_Type.click_Carrier_Type_Add_Button()
        time.sleep(2)

        # Generate a random name for the Carrier_Type code
        self.random_name = generate_random_name(10)
        self.add_Carrier_Type.enter_Carrier_Type_code(self.random_name)
        self.add_Carrier_Type.enter_Carrier_Type_des("Automation")
        self.add_Carrier_Type.click_Carrier_Type_save()
        time.sleep(5)

        Carrier_Type_add_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Carrier Type code added successfully')]")))
        act_saved_text = Carrier_Type_add_success_msg.text
        exp_saved_text = "Carrier Type code added successfully"
        if act_saved_text == exp_saved_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_add_new_Carrier_Type.png")
            self.driver.close()
            assert False


    def test_update_new_Carrier_Type(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Carrier_Type = Add_Carrier_Type_Page(self.driver)
        self.add_Carrier_Type.click_setting()
        self.add_Carrier_Type.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Carrier_Type.hover_Dis(hold_time=5)
        self.add_Carrier_Type.hover_Setup(hold_time=5)
        self.add_Carrier_Type.click_Carrier_Type()
        time.sleep(5)
        self.add_Carrier_Type.click_Carrier_Type_action_button()
        time.sleep(3)
        self.add_Carrier_Type.click_Carrier_Type_edit_info_button()
        time.sleep(3)
        self.add_Carrier_Type.enter_Carrier_Type_code("")
        time.sleep(3)
        self.add_Carrier_Type.click_Carrier_Type_update_button()
        time.sleep(5)

        Carrier_Type_update_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Carrier Type code Updated successfully')]")))
        act_saved_text = Carrier_Type_update_success_msg.text
        exp_saved_text = "Carrier Type code Updated successfully"
        if act_saved_text == exp_saved_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_update_new_Carrier_Type.png")
            self.driver.close()
            assert False


    def test_search_new_Carrier_Type(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Carrier_Type = Add_Carrier_Type_Page(self.driver)
        self.add_Carrier_Type.click_setting()
        self.add_Carrier_Type.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Carrier_Type.hover_Dis(hold_time=5)
        self.add_Carrier_Type.hover_Setup(hold_time=5)
        self.add_Carrier_Type.click_Carrier_Type()
        time.sleep(5)
        self.add_Carrier_Type.click_Carrier_Type_code_search_button()
        time.sleep(3)
        self.add_Carrier_Type.enter_Carrier_Type_code_searchbar("Carrier6")
        Carrier_Type_search_code = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(
            (By.XPATH, "//mat-cell[@data-label='code' and contains(text(), 'Carrier6')]")))
        act_Carrier_Type_search = Carrier_Type_search_code.text
        exp_Carrier_Type_search = "Carrier6"
        if act_Carrier_Type_search == exp_Carrier_Type_search:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_search_new_Carrier_Type.png")
            self.driver.close()
            assert False


    def test_delete_new_Carrier_Type(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Carrier_Type = Add_Carrier_Type_Page(self.driver)
        self.add_Carrier_Type.click_setting()
        self.add_Carrier_Type.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Carrier_Type.hover_Dis(hold_time=5)
        self.add_Carrier_Type.hover_Setup(hold_time=5)
        self.add_Carrier_Type.click_Carrier_Type()
        time.sleep(10)
        self.add_Carrier_Type.click_Carrier_Type_action_button()
        time.sleep(10)
        self.add_Carrier_Type.click_Carrier_Type_code_delete()
        time.sleep(10)
        self.add_Carrier_Type.click_Carrier_Type_code_inactive()
        time.sleep(5)

        Carrier_Type_delete_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Status updated Successfully.')]")))
        act_delete_text = Carrier_Type_delete_success_msg.text
        exp_delete_text = "Status updated Successfully."
        if act_delete_text == exp_delete_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_delete_new_Carrier_Type.png")
            self.driver.close()
            assert False


    def test_active_new_Carrier_Type(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Carrier_Type = Add_Carrier_Type_Page(self.driver)
        self.add_Carrier_Type.click_setting()
        self.add_Carrier_Type.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Carrier_Type.hover_Dis(hold_time=5)
        self.add_Carrier_Type.hover_Setup(hold_time=5)
        self.add_Carrier_Type.click_Carrier_Type()
        time.sleep(10)
        self.add_Carrier_Type.click_Carrier_Type_action_button()
        time.sleep(10)
        self.add_Carrier_Type.click_Carrier_Type_code_active()
        time.sleep(10)
        self.add_Carrier_Type.click_Carrier_Type_code_active_button()
        time.sleep(5)

        Carrier_Type_active_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Status updated Successfully.')]")))
        act_active_text = Carrier_Type_active_success_msg.text
        exp_active_text = "Status updated Successfully."
        if act_active_text == exp_active_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_active_new_Carrier_Type.png")
            self.driver.close()
            assert False
