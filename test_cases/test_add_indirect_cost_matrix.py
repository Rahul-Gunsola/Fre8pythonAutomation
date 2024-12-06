import pytest
import time
import random
import string
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Add_Indirect_Cost_Matrix import Add_Indirect_Cost_matrix_Page



def generate_random_name(self):
    letters = string.ascii_letters
    random_name = ''.join(random.choice(letters) for _ in range(self))
    return random_name



class TestAddNewCarrierRanking:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()


    def test_add_new_Indirect_Cost_matrix(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Indirect_Cost_matrix = Add_Indirect_Cost_matrix_Page(self.driver)
        self.add_Indirect_Cost_matrix.click_setting()
        self.add_Indirect_Cost_matrix.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Indirect_Cost_matrix.hover_Dis(hold_time=5)
        self.add_Indirect_Cost_matrix.hover_Setup(hold_time=5)
        self.add_Indirect_Cost_matrix.click_Indirect_Cost_matrix()
        time.sleep(5)
        self.add_Indirect_Cost_matrix.click_Indirect_Cost_matrix_Add_Button()
        time.sleep(2)

        # Generate a random name for the Indirect_Cost_matrix code
        self.random_name = generate_random_name(10)
        self.add_Indirect_Cost_matrix.enter_Indirect_Cost_matrix_number(self.random_name)
        self.add_Indirect_Cost_matrix.enter_Indirect_Cost_matrix_name(self.random_name)
        self.add_Indirect_Cost_matrix.click_Indirect_Cost_matrix_currency()
        option_to_select = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'USD - United States Dollar')]")))
        option_to_select.click()
        self.add_Indirect_Cost_matrix.enter_Indirect_Cost_matrix_description("Automation")
        self.add_Indirect_Cost_matrix.click_Indirect_Cost_matrix_calculate_by()
        per_mile_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Per Mile']")))
        per_mile_option.click()
        self.add_Indirect_Cost_matrix.enter_Indirect_Cost_matrix_highway_rate("20")
        self.add_Indirect_Cost_matrix.enter_Indirect_Cost_matrix_local_rate("10")
        self.add_Indirect_Cost_matrix.click_Indirect_Cost_matrix_save()
        time.sleep(5)

        Indirect_Cost_matrix_add_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Data Saved Successfully')]")))
        act_saved_text = Indirect_Cost_matrix_add_success_msg.text
        exp_saved_text = "Data Saved Successfully"
        if act_saved_text == exp_saved_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_add_new_Indirect_Cost_matrix.png")
            self.driver.close()
            assert False

    @pytest.mark.dispatch_setup
    def test_update_new_Indirect_Cost_matrix(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Indirect_Cost_matrix = Add_Indirect_Cost_matrix_Page(self.driver)
        self.add_Indirect_Cost_matrix.click_setting()
        self.add_Indirect_Cost_matrix.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Indirect_Cost_matrix.hover_Dis(hold_time=5)
        self.add_Indirect_Cost_matrix.hover_Setup(hold_time=5)
        self.add_Indirect_Cost_matrix.click_Indirect_Cost_matrix()
        time.sleep(5)
        self.add_Indirect_Cost_matrix.click_Indirect_Cost_matrix_action_button()
        time.sleep(3)
        self.add_Indirect_Cost_matrix.click_Indirect_Cost_matrix_edit_info_button()
        time.sleep(5)
        self.add_Indirect_Cost_matrix.enter_Indirect_Cost_matrix_number("")
        time.sleep(3)
        self.add_Indirect_Cost_matrix.click_Indirect_Cost_matrix_update_button()
        time.sleep(5)

        Indirect_Cost_matrix_update_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Data Updated Successfully')]")))
        act_saved_text = Indirect_Cost_matrix_update_success_msg.text
        exp_saved_text = "Data Updated Successfully"
        if act_saved_text == exp_saved_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_update_new_Indirect_Cost_matrix.png")
            self.driver.close()
            assert False

    @pytest.mark.dispatch_setup
    def test_search_new_Indirect_Cost_matrix(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Indirect_Cost_matrix = Add_Indirect_Cost_matrix_Page(self.driver)
        self.add_Indirect_Cost_matrix.click_setting()
        time.sleep(4)
        self.add_Indirect_Cost_matrix.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Indirect_Cost_matrix.hover_Dis(hold_time=5)
        self.add_Indirect_Cost_matrix.hover_Setup(hold_time=5)
        self.add_Indirect_Cost_matrix.click_Indirect_Cost_matrix()
        time.sleep(5)
        self.add_Indirect_Cost_matrix.click_Indirect_Cost_matrix_code_search_button()
        time.sleep(3)
        self.add_Indirect_Cost_matrix.enter_Indirect_Cost_matrix_code_searchbar("sc")
        Indirect_Cost_matrix_search_code = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//mat-row/mat-cell[normalize-space(text())='sc']")))
        act_Indirect_Cost_matrix_search = Indirect_Cost_matrix_search_code.text
        exp_Indirect_Cost_matrix_search = "sc"
        if act_Indirect_Cost_matrix_search == exp_Indirect_Cost_matrix_search:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_search_new_Indirect_Cost_matrix.png")
            self.driver.close()
            assert False

    @pytest.mark.dispatch_setup
    def test_delete_new_Indirect_Cost_matrix(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Indirect_Cost_matrix = Add_Indirect_Cost_matrix_Page(self.driver)
        self.add_Indirect_Cost_matrix.click_setting()
        self.add_Indirect_Cost_matrix.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Indirect_Cost_matrix.hover_Dis(hold_time=5)
        self.add_Indirect_Cost_matrix.hover_Setup(hold_time=5)
        self.add_Indirect_Cost_matrix.click_Indirect_Cost_matrix()
        time.sleep(10)
        self.add_Indirect_Cost_matrix.click_Indirect_Cost_matrix_action_button()
        time.sleep(10)
        self.add_Indirect_Cost_matrix.click_Indirect_Cost_matrix_code_delete()
        time.sleep(10)
        self.add_Indirect_Cost_matrix.click_Indirect_Cost_matrix_code_inactive()
        time.sleep(5)

        Indirect_Cost_matrix_delete_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Status updated Successfully.')]")))
        act_delete_text = Indirect_Cost_matrix_delete_success_msg.text
        exp_delete_text = "Status updated Successfully."
        if act_delete_text == exp_delete_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_delete_new_Indirect_Cost_matrix.png")
            self.driver.close()
            assert False

    @pytest.mark.dispatch_setup
    def test_active_new_Indirect_Cost_matrix(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Indirect_Cost_matrix = Add_Indirect_Cost_matrix_Page(self.driver)
        self.add_Indirect_Cost_matrix.click_setting()
        self.add_Indirect_Cost_matrix.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Indirect_Cost_matrix.hover_Dis(hold_time=5)
        self.add_Indirect_Cost_matrix.hover_Setup(hold_time=5)
        self.add_Indirect_Cost_matrix.click_Indirect_Cost_matrix()
        time.sleep(10)
        self.add_Indirect_Cost_matrix.click_Indirect_Cost_matrix_action_button()
        time.sleep(10)
        self.add_Indirect_Cost_matrix.click_Indirect_Cost_matrix_code_active()
        time.sleep(10)
        self.add_Indirect_Cost_matrix.click_Indirect_Cost_matrix_code_active_button()
        time.sleep(5)

        Indirect_Cost_matrix_active_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Status updated Successfully.')]")))
        act_active_text = Indirect_Cost_matrix_active_success_msg.text
        exp_active_text = "Status updated Successfully."
        if act_active_text == exp_active_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_active_new_Indirect_Cost_matrix.png")
            self.driver.close()
            assert False