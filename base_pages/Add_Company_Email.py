from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class Add_Company_Emails_Page:
    setting_button = "//button[@aria-label='Settings']"
    Dispatch_setup = "//button[@role='menuitem']//span[contains(@class, 'mat-subtitle-1') and text()=' Dispatch Setup ']"
    Company_Emails = "//a[@href='/QA/fre8/dispatch-master/dispatch-elements/manage-company-emails']"
    Company_Emails_Add_Button = "//button[contains(@class, 'header_new_btn') and contains(text(), 'Company Email')]"
    Company_Emails_Name_ID = "CompanyName"
    Company_Emails_Email_ID = "CompanyEmail"
    Company_Emails_save_button = "//button[contains(@class, 'btn-primary') and text()='Save']"
    # Company_Emails_action_button = "//mat-cell//i-tabler[@name='dots-vertical' and contains(@class, 'mat-mdc-menu-trigger')]"
    # Company_Emails_edit_info_button = "//button[.//span[text()=' Edit Info ']]"
    # Company_Emails_update_button = "//button[text()='Update' and contains(@class, 'btn-primary')]"
    Company_Emails_email_search_button = "//label[@id='CompanyEmailHeader']"
    Company_Emails_email_searchbar = "//mat-form-field[@id='CompanyEmailSearchTextBox']//input[@id='CompanyEmailInputBox']"

    # Company_Emails_code_Delete = "//i-tabler[@name='logout' and contains(@class, 'action-icons')]"
    # Company_Emails_inactive_button = "//button[contains(@class, 'swal2-confirm') and contains(text(), 'Yes, Mark as Inactive!')]"
    # Company_Emails_code_Active = "//i-tabler[@name='logout-2' and contains(@class, 'action-icons')]"
    # Company_Emails_active_button = "//button[contains(@class, 'swal2-confirm') and contains(text(), 'Yes, Mark as Active!')]"

    def __init__(self, driver):
        self.driver = driver

    def click_setting(self):
        self.driver.find_element(By.XPATH, self.setting_button).click()

    def click_dispatch_setup(self):
        self.driver.find_element(By.XPATH, self.Dispatch_setup).click()

    def click_Company_Emails(self):
        self.driver.find_element(By.XPATH, self.Company_Emails).click()

    def click_Company_Emails_Add_Button(self):
        self.driver.find_element(By.XPATH, self.Company_Emails_Add_Button).click()

    def enter_Company_Emails_Email(self, email):
        self.driver.find_element(By.ID, self.Company_Emails_Email_ID).send_keys(email)

    def enter_Company_Emails_Name(self, name):
        self.driver.find_element(By.ID, self.Company_Emails_Name_ID).send_keys(name)

    def click_Company_Emails_save(self):
        self.driver.find_element(By.XPATH, self.Company_Emails_save_button).click()

    # def click_Company_Emails_action_button(self):
    #     self.driver.find_element(By.XPATH, self.Company_Emails_action_button).click()
    #
    # def click_Company_Emails_edit_info_button(self):
    #     self.driver.find_element(By.XPATH, self.Company_Emails_edit_info_button).click()
    #
    # def click_Company_Emails_update_button(self):
    #     self.driver.find_element(By.XPATH, self.Company_Emails_update_button).click()

    def click_Company_Emails_email_search_button(self):
        self.driver.find_element(By.XPATH, self.Company_Emails_email_search_button).click()

    def enter_Company_Emails_email_searchbar(self, email):
        self.driver.find_element(By.XPATH, self.Company_Emails_email_searchbar).send_keys(email)

    # def click_Company_Emails_code_delete(self):
    #     self.driver.find_element(By.XPATH, self.Company_Emails_code_Delete).click()
    #
    # def click_Company_Emails_code_inactive(self):
    #     self.driver.find_element(By.XPATH, self.Company_Emails_inactive_button).click()
    #
    # def click_Company_Emails_code_active(self):
    #     self.driver.find_element(By.XPATH, self.Company_Emails_code_Active).click()
    #
    # def click_Company_Emails_code_active_button(self):
    #     self.driver.find_element(By.XPATH, self.Company_Emails_active_button).click()