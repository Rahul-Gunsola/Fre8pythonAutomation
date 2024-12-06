import pytest
import time
import random
import string
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Add_Carrier_Ranking import Add_Carrier_Ranking_Page

used_numbers = set()  # To track the numbers that have been used


def generate_random_name(self):
    letters = string.ascii_letters
    random_name = ''.join(random.choice(letters) for _ in range(self))
    return random_name


def get_unique_number():
    while True:
        number = random.randint(1, 1000)  # Generate a random number between 1 and 1000
        if number not in used_numbers:  # Check if the number has been used before
            used_numbers.add(number)  # Mark the number as used
            return number  # Return the unique number


class TestAddNewCarrierRanking:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()

    def test_add_new_Carrier_Ranking(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Carrier_Ranking = Add_Carrier_Ranking_Page(self.driver)
        self.add_Carrier_Ranking.click_setting()
        self.add_Carrier_Ranking.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Carrier_Ranking.hover_Dis(hold_time=5)
        self.add_Carrier_Ranking.hover_Setup(hold_time=5)
        self.add_Carrier_Ranking.click_Carrier_Ranking()
        time.sleep(5)
        self.add_Carrier_Ranking.click_Carrier_Ranking_Add_Button()
        time.sleep(2)

        # Generate a random name for the Carrier_Ranking code
        self.random_name = generate_random_name(10)
        self.add_Carrier_Ranking.enter_Carrier_Ranking_code(self.random_name)
        # Generate a unique number for Carrier_Ranking order
        self.unique_number = str(get_unique_number())
        self.add_Carrier_Ranking.enter_Carrier_Ranking_order(self.unique_number)
        self.add_Carrier_Ranking.enter_Carrier_Ranking_des("Automation")
        self.add_Carrier_Ranking.click_Carrier_Ranking_save()
        time.sleep(5)

        Carrier_Ranking_add_success_msg = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Carrier Ranking added successfully')]")))
        act_saved_text = Carrier_Ranking_add_success_msg.text
        exp_saved_text = "Carrier Ranking added successfully"
        if act_saved_text == exp_saved_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_add_new_Carrier_Ranking.png")
            self.driver.close()
            assert False

    def test_update_new_Carrier_Ranking(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Carrier_Ranking = Add_Carrier_Ranking_Page(self.driver)
        self.add_Carrier_Ranking.click_setting()
        self.add_Carrier_Ranking.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Carrier_Ranking.hover_Dis(hold_time=5)
        self.add_Carrier_Ranking.hover_Setup(hold_time=5)
        self.add_Carrier_Ranking.click_Carrier_Ranking()
        time.sleep(5)
        self.add_Carrier_Ranking.click_Carrier_Ranking_action_button()
        time.sleep(3)
        self.add_Carrier_Ranking.click_Carrier_Ranking_edit_info_button()
        time.sleep(3)
        self.add_Carrier_Ranking.enter_Carrier_Ranking_code("")
        time.sleep(3)
        self.add_Carrier_Ranking.click_Carrier_Ranking_update_button()
        time.sleep(5)

        Carrier_Ranking_update_success_msg = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//div[@id='toast-container']//div[contains(text(), 'Carrier Ranking updated successfully')]")))
        act_saved_text = Carrier_Ranking_update_success_msg.text
        exp_saved_text = "Carrier Ranking updated successfully"
        if act_saved_text == exp_saved_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_update_new_Carrier_Ranking.png")
            self.driver.close()
            assert False

    def test_search_new_Carrier_Ranking(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Carrier_Ranking = Add_Carrier_Ranking_Page(self.driver)
        self.add_Carrier_Ranking.click_setting()
        self.add_Carrier_Ranking.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Carrier_Ranking.hover_Dis(hold_time=5)
        self.add_Carrier_Ranking.hover_Setup(hold_time=5)
        self.add_Carrier_Ranking.click_Carrier_Ranking()
        time.sleep(5)
        self.add_Carrier_Ranking.click_Carrier_Ranking_code_search_button()
        time.sleep(3)
        self.add_Carrier_Ranking.enter_Carrier_Ranking_code_searchbar("pop")
        Carrier_Ranking_search_code = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located((By.XPATH, "//mat-cell[@data-label='code' and contains(text(), 'pop')]")))
        act_Carrier_Ranking_search = Carrier_Ranking_search_code.text
        exp_Carrier_Ranking_search = "pop"
        if act_Carrier_Ranking_search == exp_Carrier_Ranking_search:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_search_new_Carrier_Ranking.png")
            self.driver.close()
            assert False

    def test_delete_new_Carrier_Ranking(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Carrier_Ranking = Add_Carrier_Ranking_Page(self.driver)
        self.add_Carrier_Ranking.click_setting()
        self.add_Carrier_Ranking.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Carrier_Ranking.hover_Dis(hold_time=5)
        self.add_Carrier_Ranking.hover_Setup(hold_time=5)
        self.add_Carrier_Ranking.click_Carrier_Ranking()
        time.sleep(10)
        self.add_Carrier_Ranking.click_Carrier_Ranking_action_button()
        time.sleep(10)
        self.add_Carrier_Ranking.click_Carrier_Ranking_code_delete()
        time.sleep(10)
        self.add_Carrier_Ranking.click_Carrier_Ranking_code_inactive()
        time.sleep(5)

        Carrier_Ranking_delete_success_msg = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Status updated successfully')]")))
        act_delete_text = Carrier_Ranking_delete_success_msg.text
        exp_delete_text = "Status updated successfully"
        if act_delete_text == exp_delete_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_delete_new_Carrier_Ranking.png")
            self.driver.close()
            assert False

    def test_active_new_Carrier_Ranking(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)

        self.add_Carrier_Ranking = Add_Carrier_Ranking_Page(self.driver)
        self.add_Carrier_Ranking.click_setting()
        self.add_Carrier_Ranking.click_Dispatch_Setup()
        time.sleep(5)
        self.add_Carrier_Ranking.hover_Dis(hold_time=5)
        self.add_Carrier_Ranking.hover_Setup(hold_time=5)
        self.add_Carrier_Ranking.click_Carrier_Ranking()
        time.sleep(10)
        self.add_Carrier_Ranking.click_Carrier_Ranking_action_button()
        time.sleep(10)
        self.add_Carrier_Ranking.click_Carrier_Ranking_code_active()
        time.sleep(10)
        self.add_Carrier_Ranking.click_Carrier_Ranking_code_active_button()
        time.sleep(5)

        Carrier_Ranking_active_success_msg = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@id='toast-container']//div[contains(text(), 'Status updated successfully')]")))
        act_active_text = Carrier_Ranking_active_success_msg.text
        exp_active_text = "Status updated successfully"
        if act_active_text == exp_active_text:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_active_new_Carrier_Ranking.png")
            self.driver.close()
            assert False
