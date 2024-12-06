import pytest
import time
import random
import string
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Add_Company_Emails import Add_Company_Emails_Page


def generate_random_name(self):
    letters = string.ascii_letters
    random_name = ''.join(random.choice(letters) for _ in range(self))
    return random_name

def generate_random_email():
    letters = string.ascii_lowercase
    random_name = ''.join(random.choice(letters) for _ in range(10))
    return f"{random_name}@gmail.com"

class TestAddNewCompanyEmail:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()

    @pytest.mark.dispatch_setup
    def test_add_new_Company_Emails(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Company_Emails = Add_Company_Emails_Page(self.driver)
        self.add_Company_Emails.click_setting()
        self.add_Company_Emails.click_dispatch_setup()
        time.sleep(10)
        self.add_Company_Emails.click_Company_Emails()
        time.sleep(5)
        self.add_Company_Emails.click_Company_Emails_Add_Button()
        time.sleep(2)

        # Generate a random Company name for the Company_Emails
        self.random_name = generate_random_name(10)
        # Generate a random Company email with gmail.com domain
        self.random_email = generate_random_email()
        self.add_Company_Emails.enter_Company_Emails_Email(self.random_email)
        self.add_Company_Emails.enter_Company_Emails_Name(self.random_name)
        self.add_Company_Emails.click_Company_Emails_save()
        time.sleep(5)

        Company_Emails_add_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Verification email sent! Please check your inbox to Verify your account.')]")))
        act_saved_text = Company_Emails_add_success_msg.text
        exp_saved_text = "Verification email sent! Please check your inbox to Verify your account."
        if act_saved_text == exp_saved_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_add_new_Company_Emails.png")
            self.driver.close()
            assert False

    # @pytest.mark.dispatch_setup
    # def test_update_new_Company_Emails(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.admin_page_url)
    #     self.admin_lp = Login_Admin_Page(self.driver)
    #     self.admin_lp.enter_username(self.username)
    #     self.admin_lp.enter_password(self.password)
    #     self.admin_lp.click_login()
    #     self.driver.maximize_window()
    #     time.sleep(10)
    #
    #     self.add_Company_Emails = Add_Company_Emails_Page(self.driver)
    #     self.add_Company_Emails.click_setting()
    #     self.add_Company_Emails.click_dispatch_setup()
    #     time.sleep(10)
    #     self.add_Company_Emails.click_Company_Emails()
    #     time.sleep(5)
    #     self.add_Company_Emails.click_Company_Emails_action_button()
    #     time.sleep(3)
    #     self.add_Company_Emails.click_Company_Emails_edit_info_button()
    #     time.sleep(3)
    #     self.add_Company_Emails.enter_Company_Emails_code("")
    #     time.sleep(3)
    #     self.add_Company_Emails.click_Company_Emails_update_button()
    #     time.sleep(5)
    #
    #     Company_Emails_update_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Carrier Ranking updated successfully')]")))
    #     act_saved_text = Company_Emails_update_success_msg.text
    #     exp_saved_text = "Carrier Ranking updated successfully"
    #     if act_saved_text == exp_saved_text:
    #         assert True
    #         self.driver.close()
    #
    #     else:
    #         self.driver.save_screenshot(".\\screenshots\\test_update_new_Company_Emails.png")
    #         self.driver.close()
    #         assert False

    @pytest.mark.dispatch_setup
    def test_search_new_Company_Emails(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Company_Emails = Add_Company_Emails_Page(self.driver)
        self.add_Company_Emails.click_setting()
        self.add_Company_Emails.click_dispatch_setup()
        time.sleep(10)
        self.add_Company_Emails.click_Company_Emails()
        time.sleep(5)
        self.add_Company_Emails.click_Company_Emails_email_search_button()
        time.sleep(3)
        self.add_Company_Emails.enter_Company_Emails_email_searchbar("rahulgunsola09@gmail.com")
        time.sleep(3)
        Company_Emails_search_email = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//mat-cell[contains(@class, 'mat-mdc-cell') and contains(text(), 'rahulgunsola09@gmail.com')]")))
        act_Company_Emails_search = Company_Emails_search_email.text
        exp_Company_Emails_search = "rahulgunsola09@gmail.com"
        if act_Company_Emails_search == exp_Company_Emails_search:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_search_new_Company_Emails.png")
            self.driver.close()
            assert False

    # @pytest.mark.dispatch_setup
    # def test_delete_new_Company_Emails(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.admin_page_url)
    #     self.admin_lp = Login_Admin_Page(self.driver)
    #     self.admin_lp.enter_username(self.username)
    #     self.admin_lp.enter_password(self.password)
    #     self.admin_lp.click_login()
    #     self.driver.maximize_window()
    #     time.sleep(10)
    #
    #     self.add_Company_Emails = Add_Company_Emails_Page(self.driver)
    #     self.add_Company_Emails.click_setting()
    #     self.add_Company_Emails.click_dispatch_setup()
    #     time.sleep(10)
    #     self.add_Company_Emails.click_Company_Emails()
    #     time.sleep(10)
    #     self.add_Company_Emails.click_Company_Emails_action_button()
    #     time.sleep(10)
    #     self.add_Company_Emails.click_Company_Emails_code_delete()
    #     time.sleep(10)
    #     self.add_Company_Emails.click_Company_Emails_code_inactive()
    #     time.sleep(5)
    #
    #     Company_Emails_delete_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Status updated successfully')]")))
    #     act_delete_text = Company_Emails_delete_success_msg.text
    #     exp_delete_text = "Status updated successfully"
    #     if act_delete_text == exp_delete_text:
    #         assert True
    #         self.driver.close()
    #
    #     else:
    #         self.driver.save_screenshot(".\\screenshots\\test_delete_new_Company_Emails.png")
    #         self.driver.close()
    #         assert False
    #
    # @pytest.mark.dispatch_setup
    # def test_active_new_Company_Emails(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.admin_page_url)
    #     self.admin_lp = Login_Admin_Page(self.driver)
    #     self.admin_lp.enter_username(self.username)
    #     self.admin_lp.enter_password(self.password)
    #     self.admin_lp.click_login()
    #     self.driver.maximize_window()
    #     time.sleep(10)
    #
    #     self.add_Company_Emails = Add_Company_Emails_Page(self.driver)
    #     self.add_Company_Emails.click_setting()
    #     self.add_Company_Emails.click_dispatch_setup()
    #     time.sleep(10)
    #     self.add_Company_Emails.click_Company_Emails()
    #     time.sleep(10)
    #     self.add_Company_Emails.click_Company_Emails_action_button()
    #     time.sleep(10)
    #     self.add_Company_Emails.click_Company_Emails_code_active()
    #     time.sleep(10)
    #     self.add_Company_Emails.click_Company_Emails_code_active_button()
    #     time.sleep(5)
    #
    #     Company_Emails_active_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Status updated successfully')]")))
    #     act_active_text = Company_Emails_active_success_msg.text
    #     exp_active_text = "Status updated successfully"
    #     if act_active_text == exp_active_text:
    #         assert True
    #         self.driver.close()
    #
    #     else:
    #         self.driver.save_screenshot(".\\screenshots\\test_active_new_Company_Emails.png")
    #         self.driver.close()
    #         assert False