import random
import string
import time
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Add_Designation import Add_Designation_Page


def generate_random_name(self):
    letters = string.ascii_letters
    random_name = ''.join(random.choice(letters) for _ in range(self))
    return random_name

class TestAddNewDesignation:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()


    def test_add_new_designation(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_designation = Add_Designation_Page(self.driver)
        self.add_designation.click_setting()
        time.sleep(5)
        self.add_designation.click_Organization()
        time.sleep(5)
        self.add_designation.hover_organization(hold_time=5)
        self.add_designation.click_designation()
        time.sleep(5)
        self.add_designation.click_designation_Add_Button()
        time.sleep(2)

        # Generate a random name for the designation code
        self.random_name = generate_random_name(10)
        self.add_designation.enter_designation_code(self.random_name)
        self.add_designation.enter_designation_des("Automation")
        self.add_designation.click_designation_save()
        time.sleep(5)

        designation_add_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Designation saved successfully')]")))
        act_saved_text = designation_add_success_msg.text
        exp_saved_text = "Designation saved successfully"
        if act_saved_text == exp_saved_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_add_new_designation.png")
            self.driver.close()
            assert False


    def test_update_new_designation(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_designation = Add_Designation_Page(self.driver)
        self.add_designation.click_setting()
        self.add_designation.click_Organization()
        time.sleep(5)
        self.add_designation.hover_organization(hold_time=5)
        self.add_designation.click_designation()
        time.sleep(15)
        self.add_designation.click_designation_action_button()
        time.sleep(3)
        self.add_designation.click_designation_edit_info_button()
        time.sleep(3)
        self.add_designation.enter_designation_code("")
        time.sleep(3)
        self.add_designation.click_designation_update_button()
        time.sleep(5)

        designation_update_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Designation Updated successfully')]")))
        act_saved_text = designation_update_success_msg.text
        exp_saved_text = "Designation Updated successfully"
        if act_saved_text == exp_saved_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_update_new_designation.png")
            self.driver.close()
            assert False


    def test_search_new_designation(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_designation = Add_Designation_Page(self.driver)
        self.add_designation.click_setting()
        self.add_designation.click_Organization()
        time.sleep(5)
        self.add_designation.hover_organization(hold_time=5)
        self.add_designation.click_designation()
        time.sleep(15)
        self.add_designation.click_designation_code_search_button()
        time.sleep(3)
        self.add_designation.enter_designation_code_searchbar("Mech")
        designation_search_code = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//mat-cell[@data-label='DesignationCode' and contains(text(), 'Mech')]")))
        act_designation_search = designation_search_code.text
        exp_designation_search = "Mech"
        if act_designation_search == exp_designation_search:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_search_new_designation.png")
            self.driver.close()
            assert False


    def test_delete_new_designation(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_designation = Add_Designation_Page(self.driver)
        self.add_designation.click_setting()
        self.add_designation.click_Organization()
        time.sleep(5)
        self.add_designation.hover_organization(hold_time=5)
        self.add_designation.click_designation()
        time.sleep(10)
        self.add_designation.click_designation_action_button()
        time.sleep(10)
        self.add_designation.click_designation_code_delete()
        time.sleep(10)
        self.add_designation.click_designation_code_inactive()
        time.sleep(5)

        designation_delete_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Status updated Successfully.')]")))
        act_delete_text = designation_delete_success_msg.text
        exp_delete_text = "Status updated Successfully."
        if act_delete_text == exp_delete_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_delete_new_designation.png")
            self.driver.close()
            assert False


    def test_active_new_designation(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_designation = Add_Designation_Page(self.driver)
        self.add_designation.click_setting()
        self.add_designation.click_Organization()
        time.sleep(5)
        self.add_designation.hover_organization(hold_time=5)
        self.add_designation.click_designation()
        time.sleep(10)
        self.add_designation.click_designation_action_button()
        time.sleep(10)
        self.add_designation.click_designation_code_active()
        time.sleep(10)
        self.add_designation.click_designation_code_active_button()
        time.sleep(5)

        designation_active_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Status updated Successfully.')]")))
        act_active_text = designation_active_success_msg.text
        exp_active_text = "Status updated Successfully."
        if act_active_text == exp_active_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_active_new_designation.png")
            self.driver.close()
            assert False