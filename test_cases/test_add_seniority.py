import pytest
import time
import random
import string
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Add_Seniority import Add_Seniority_Page


def generate_random_code(self):
    letters = string.ascii_letters
    random_code = ''.join(random.choice(letters) for _ in range(self))
    return random_code


class TestAddNewSeniority:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()

    def test_add_new_Seniority(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Seniority = Add_Seniority_Page(self.driver)
        self.add_Seniority.click_setting()
        self.add_Seniority.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Seniority.hover_Dis(hold_time=5)
        self.add_Seniority.hover_Setup(hold_time=5)
        self.add_Seniority.click_Seniority()
        time.sleep(5)
        self.add_Seniority.click_Seniority_Add_Button()
        time.sleep(2)

        # Generate a random name for the Seniority code
        self.random_code = generate_random_code(6)
        self.add_Seniority.enter_Seniority_code(self.random_code)
        self.add_Seniority.enter_Seniority_From("1")
        self.add_Seniority.enter_Seniority_To("2")
        self.add_Seniority.click_Seniority_save()
        time.sleep(5)

        Seniority_add_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Seniority code added successfully')]")))
        act_saved_text = Seniority_add_success_msg.text
        exp_saved_text = "Seniority code added successfully"
        if act_saved_text == exp_saved_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_add_new_Seniority.png")
            self.driver.close()
            assert False


    def test_update_new_Seniority(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        time.sleep(10)

        self.add_Seniority = Add_Seniority_Page(self.driver)
        self.add_Seniority.click_setting()
        self.add_Seniority.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Seniority.hover_Dis(hold_time=5)
        self.add_Seniority.hover_Setup(hold_time=5)
        self.add_Seniority.click_Seniority()
        time.sleep(5)
        self.add_Seniority.click_Seniority_action_button()
        time.sleep(3)
        self.add_Seniority.click_Seniority_edit_info_button()
        time.sleep(3)
        self.add_Seniority.enter_Seniority_code("")
        time.sleep(3)
        self.add_Seniority.click_Seniority_update_button()
        time.sleep(5)

        Seniority_update_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Seniority code updated successfully')]")))
        act_saved_text = Seniority_update_success_msg.text
        exp_saved_text = "Seniority code updated successfully"
        if act_saved_text == exp_saved_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_update_new_Seniority.png")
            self.driver.close()
            assert False


    def test_search_new_Seniority(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Seniority = Add_Seniority_Page(self.driver)
        self.add_Seniority.click_setting()
        self.add_Seniority.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Seniority.hover_Dis(hold_time=5)
        self.add_Seniority.hover_Setup(hold_time=5)
        self.add_Seniority.click_Seniority()
        time.sleep(5)
        self.add_Seniority.click_Seniority_code_search_button()
        time.sleep(3)
        self.add_Seniority.enter_Seniority_code_searchbar("Fresher")
        Seniority_search_code = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(
            (By.XPATH, "//mat-cell[@data-label='SeniorityCode' and contains(text(), 'Fresher')]")))
        act_Seniority_search = Seniority_search_code.text
        exp_Seniority_search = "Fresher"
        if act_Seniority_search == exp_Seniority_search:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_search_new_Seniority.png")
            self.driver.close()
            assert False


    def test_delete_new_Seniority(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Seniority = Add_Seniority_Page(self.driver)
        self.add_Seniority.click_setting()
        self.add_Seniority.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Seniority.hover_Dis(hold_time=5)
        self.add_Seniority.hover_Setup(hold_time=5)
        self.add_Seniority.click_Seniority()
        time.sleep(10)
        self.add_Seniority.click_Seniority_action_button()
        time.sleep(10)
        self.add_Seniority.click_Seniority_code_delete()
        time.sleep(10)
        self.add_Seniority.click_Seniority_code_inactive()
        time.sleep(5)

        Seniority_delete_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Status updated Successfully.')]")))
        act_delete_text = Seniority_delete_success_msg.text
        exp_delete_text = "Status updated Successfully."
        if act_delete_text == exp_delete_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_delete_new_Seniority.png")
            self.driver.close()
            assert False


    def test_active_new_Seniority(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Seniority = Add_Seniority_Page(self.driver)
        self.add_Seniority.click_setting()
        self.add_Seniority.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Seniority.hover_Dis(hold_time=5)
        self.add_Seniority.hover_Setup(hold_time=5)
        self.add_Seniority.click_Seniority()
        time.sleep(10)
        self.add_Seniority.click_Seniority_action_button()
        time.sleep(10)
        self.add_Seniority.click_Seniority_code_active()
        time.sleep(10)
        self.add_Seniority.click_Seniority_code_active_button()
        time.sleep(5)

        Seniority_active_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Status updated Successfully.')]")))
        act_active_text = Seniority_active_success_msg.text
        exp_active_text = "Status updated Successfully."
        if act_active_text == exp_active_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_active_new_Seniority.png")
            self.driver.close()
            assert False
