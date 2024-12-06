import pytest
import time
import random
import string
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Add_units_Of_Measurement import Add_Units_Of_Measurement_Page


def generate_random_name(self):
    letters = string.ascii_letters
    random_name = ''.join(random.choice(letters) for _ in range(self))
    return random_name


class TestAddNewUnitOfMeasurement:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()


    def test_add_new_Unit_Of_Measurement(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Unit_Of_Measurement = Add_Units_Of_Measurement_Page(self.driver)
        self.add_Unit_Of_Measurement.click_setting()
        self.add_Unit_Of_Measurement.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Unit_Of_Measurement.hover_Dis(hold_time=5)
        self.add_Unit_Of_Measurement.hover_Setup(hold_time=5)
        self.add_Unit_Of_Measurement.click_Unit_Of_Measurement()
        time.sleep(5)
        self.add_Unit_Of_Measurement.click_Unit_Of_Measurement_Add_Button()
        time.sleep(2)

        # Generate a random name for the Unit_Of_Measurement code
        self.random_name = generate_random_name(10)
        self.add_Unit_Of_Measurement.enter_Unit_Of_Measurement_Name(self.random_name)
        self.add_Unit_Of_Measurement.enter_Unit_Of_Measurement_Symbol(self.random_name)
        self.add_Unit_Of_Measurement.click_Unit_Of_Measurement_save()
        time.sleep(5)

        Unit_Of_Measurement_add_success_msg = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'UOM name saved successfully')]")))
        act_saved_text = Unit_Of_Measurement_add_success_msg.text
        exp_saved_text = "UOM name saved successfully"
        if act_saved_text == exp_saved_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_add_new_Unit_Of_Measurement.png")
            self.driver.close()
            assert False


    def test_update_new_Unit_Of_Measurement(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Unit_Of_Measurement = Add_Units_Of_Measurement_Page(self.driver)
        self.add_Unit_Of_Measurement.click_setting()
        self.add_Unit_Of_Measurement.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Unit_Of_Measurement.hover_Dis(hold_time=5)
        self.add_Unit_Of_Measurement.hover_Setup(hold_time=5)
        self.add_Unit_Of_Measurement.click_Unit_Of_Measurement()
        time.sleep(5)
        self.add_Unit_Of_Measurement.click_Unit_Of_Measurement_action_button()
        time.sleep(3)
        self.add_Unit_Of_Measurement.click_Unit_Of_Measurement_edit_info_button()
        time.sleep(3)
        self.add_Unit_Of_Measurement.enter_Unit_Of_Measurement_Name("")
        time.sleep(3)
        self.add_Unit_Of_Measurement.click_Unit_Of_Measurement_update_button()
        time.sleep(5)

        Unit_Of_Measurement_update_success_msg = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'UOM Updated successfully')]")))
        act_saved_text = Unit_Of_Measurement_update_success_msg.text
        exp_saved_text = "UOM Updated successfully"
        if act_saved_text == exp_saved_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_update_new_Unit_Of_Measurement.png")
            self.driver.close()
            assert False


    def test_search_new_Unit_Of_Measurement(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Unit_Of_Measurement = Add_Units_Of_Measurement_Page(self.driver)
        self.add_Unit_Of_Measurement.click_setting()
        self.add_Unit_Of_Measurement.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Unit_Of_Measurement.hover_Dis(hold_time=5)
        self.add_Unit_Of_Measurement.hover_Setup(hold_time=5)
        self.add_Unit_Of_Measurement.click_Unit_Of_Measurement()
        time.sleep(5)
        self.add_Unit_Of_Measurement.click_Unit_Of_Measurement_code_search_button()
        time.sleep(3)
        self.add_Unit_Of_Measurement.enter_Unit_Of_Measurement_code_searchbar("litre")
        Unit_Of_Measurement_search_code = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(
            (By.XPATH, "//mat-cell[@data-label='UOMName' and contains(text(), 'litre')]")))
        act_Unit_Of_Measurement_search = Unit_Of_Measurement_search_code.text
        exp_Unit_Of_Measurement_search = "litre"
        if act_Unit_Of_Measurement_search == exp_Unit_Of_Measurement_search:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_search_new_Unit_Of_Measurement.png")
            self.driver.close()
            assert False


    def test_delete_new_Unit_Of_Measurement(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Unit_Of_Measurement = Add_Units_Of_Measurement_Page(self.driver)
        self.add_Unit_Of_Measurement.click_setting()
        self.add_Unit_Of_Measurement.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Unit_Of_Measurement.hover_Dis(hold_time=5)
        self.add_Unit_Of_Measurement.hover_Setup(hold_time=5)
        self.add_Unit_Of_Measurement.click_Unit_Of_Measurement()
        time.sleep(10)
        self.add_Unit_Of_Measurement.click_Unit_Of_Measurement_action_button()
        time.sleep(10)
        self.add_Unit_Of_Measurement.click_Unit_Of_Measurement_code_delete()
        time.sleep(10)
        self.add_Unit_Of_Measurement.click_Unit_Of_Measurement_code_inactive()
        time.sleep(5)

        Unit_Of_Measurement_delete_success_msg = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Status updated successfully')]")))
        act_delete_text = Unit_Of_Measurement_delete_success_msg.text
        exp_delete_text = "Status updated successfully"
        if act_delete_text == exp_delete_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_delete_new_Unit_Of_Measurement.png")
            self.driver.close()
            assert False


    def test_active_new_Unit_Of_Measurement(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Unit_Of_Measurement = Add_Units_Of_Measurement_Page(self.driver)
        self.add_Unit_Of_Measurement.click_setting()
        self.add_Unit_Of_Measurement.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Unit_Of_Measurement.hover_Dis(hold_time=5)
        self.add_Unit_Of_Measurement.hover_Setup(hold_time=5)
        self.add_Unit_Of_Measurement.click_Unit_Of_Measurement()
        time.sleep(10)
        self.add_Unit_Of_Measurement.click_Unit_Of_Measurement_action_button()
        time.sleep(10)
        self.add_Unit_Of_Measurement.click_Unit_Of_Measurement_code_active()
        time.sleep(10)
        self.add_Unit_Of_Measurement.click_Unit_Of_Measurement_code_active_button()
        time.sleep(5)

        Unit_Of_Measurement_active_success_msg = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Status updated successfully')]")))
        act_active_text = Unit_Of_Measurement_active_success_msg.text
        exp_active_text = "Status updated successfully"
        if act_active_text == exp_active_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_active_new_Unit_Of_Measurement.png")
            self.driver.close()
            assert False
