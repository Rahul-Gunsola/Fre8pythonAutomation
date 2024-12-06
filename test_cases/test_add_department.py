import random
import string
import time
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Add_Department import Add_Department_Page


def generate_random_name(self):
    letters = string.ascii_letters
    random_name = ''.join(random.choice(letters) for _ in range(self))
    return random_name

class TestAddNewDepartment:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()

    # @pytest.mark.dispatch_setup
    def test_add_new_department(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_department = Add_Department_Page(self.driver)
        self.add_department.click_setting()
        time.sleep(5)
        self.add_department.click_Organization()
        time.sleep(5)
        self.add_department.hover_organization(hold_time=5)
        self.add_department.click_department()
        time.sleep(15)
        self.add_department.click_department_Add_Button()
        time.sleep(2)

        # Generate a random name for the department code
        self.random_name = generate_random_name(10)
        self.add_department.enter_department_code(self.random_name)
        self.add_department.enter_department_des("Automation")
        self.add_department.click_department_save()
        time.sleep(5)

        department_add_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Department saved successfully')]")))
        act_saved_text = department_add_success_msg.text
        exp_saved_text = "Department saved successfully"
        if act_saved_text == exp_saved_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_add_new_department.png")
            self.driver.close()
            assert False


    def test_update_new_department(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_department = Add_Department_Page(self.driver)
        self.add_department.click_setting()
        self.add_department.click_Organization()
        time.sleep(5)
        self.add_department.hover_organization(hold_time=5)
        self.add_department.click_department()
        time.sleep(15)
        self.add_department.click_department_action_button()
        time.sleep(3)
        self.add_department.click_department_edit_info_button()
        time.sleep(3)
        self.add_department.enter_department_code("")
        time.sleep(3)
        self.add_department.click_department_update_button()
        time.sleep(5)

        department_update_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Department updated successfully')]")))
        act_saved_text = department_update_success_msg.text
        exp_saved_text = "Department updated successfully"
        if act_saved_text == exp_saved_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_update_new_department.png")
            self.driver.close()
            assert False


    def test_search_new_department(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_department = Add_Department_Page(self.driver)
        self.add_department.click_setting()
        self.add_department.click_Organization()
        time.sleep(5)
        self.add_department.hover_organization(hold_time=5)
        self.add_department.click_department()
        time.sleep(15)
        self.add_department.click_department_code_search_button()
        time.sleep(3)
        self.add_department.enter_department_code_searchbar("Accountant112")
        department_search_code = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//mat-cell[@data-label='DepartmentCode' and contains(text(), 'Accountant112')]")))
        act_department_search = department_search_code.text
        exp_department_search = "Accountant112"
        if act_department_search == exp_department_search:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_search_new_department.png")
            self.driver.close()
            assert False


    def test_delete_new_department(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_department = Add_Department_Page(self.driver)
        self.add_department.click_setting()
        self.add_department.click_Organization()
        time.sleep(5)
        self.add_department.hover_organization(hold_time=5)
        self.add_department.click_department()
        time.sleep(15)
        self.add_department.click_department_action_button()
        time.sleep(10)
        self.add_department.click_department_code_delete()
        time.sleep(10)
        self.add_department.click_department_code_inactive()
        time.sleep(5)

        department_delete_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Status updated Successfully.')]")))
        act_delete_text = department_delete_success_msg.text
        exp_delete_text = "Status updated Successfully."
        if act_delete_text == exp_delete_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_delete_new_department.png")
            self.driver.close()
            assert False


    def test_active_new_department(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_department = Add_Department_Page(self.driver)
        self.add_department.click_setting()
        self.add_department.click_Organization()
        time.sleep(5)
        self.add_department.hover_organization(hold_time=5)
        self.add_department.click_department()
        time.sleep(15)
        self.add_department.click_department_action_button()
        time.sleep(10)
        self.add_department.click_department_code_active()
        time.sleep(10)
        self.add_department.click_department_code_active_button()
        time.sleep(5)

        department_active_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Status updated Successfully.')]")))
        act_active_text = department_active_success_msg.text
        exp_active_text = "Status updated Successfully."
        if act_active_text == exp_active_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_active_new_department.png")
            self.driver.close()
            assert False