from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class Add_Seniority_Page:
    setting_button = "//button[@aria-label='Settings']"
    Dispatch_Setup = "//span[contains(@class, 'mat-subtitle-1') and contains(text(), 'Dispatch')]"
    hover_Dispatch = "//span[contains(@class, 'sidebar-element-name') and text()='Dispatch ']"
    hover_Dispatch_Setup = "//label[contains(@class, 'sidebar-element-name') and text()='Dispatch Setup']"
    Seniority = "//label[text()='Seniority Codes ']"
    Seniority_Add_Button = "//button[contains(@class, 'header_new_btn') and contains(text(), 'Seniority')]"
    Seniority_Code_ID = "seniorityCode"
    Seniority_From_ID = "fromYear"
    Seniority_To_ID = "toYear"
    Seniority_save_button = "//button[contains(@class, 'btn-primary') and text()='Save']"
    Seniority_action_button = "//mat-cell//i-tabler[@name='dots-vertical' and contains(@class, 'mat-mdc-menu-trigger')]"
    Seniority_edit_info_button = "//button[.//span[text()=' Edit Info ']]"
    Seniority_update_button = "//button[text()='Update' and contains(@class, 'btn-primary')]"
    Seniority_code_search_button = "//label[@id='NameHeader']"
    Seniority_code_searchbar = "//mat-form-field[@id='NameSearchTextBox']//input[@id='NameInputBox']"
    Seniority_code_Delete = "//i-tabler[@name='logout' and contains(@class, 'action-icons')]"
    Seniority_inactive_button = "//button[contains(@class, 'swal2-confirm') and contains(text(), 'Yes, Mark as Inactive!')]"
    Seniority_code_Active = "//i-tabler[@name='logout-2' and contains(@class, 'action-icons')]"
    Seniority_active_button = "//button[contains(@class, 'swal2-confirm') and contains(text(), 'Yes, Mark as Active!')]"

    def __init__(self, driver):
        self.driver = driver

    def click_setting(self):
        self.driver.find_element(By.XPATH, self.setting_button).click()

    def click_Dispatch_Setup(self):
        # Click on the Dispatch menu
        self.driver.find_element(By.XPATH, self.Dispatch_Setup).click()

    def hover_Dis(self, hold_time=5):
        # Hover over the "Dispatch" sidebar menu
        hover_element = self.driver.find_element(By.XPATH, self.hover_Dispatch)
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_element).perform()
        time.sleep(hold_time)

    def hover_Setup(self, hold_time=5):
        # Hover over the organization sidebar menu
        hover_element = self.driver.find_element(By.XPATH, self.hover_Dispatch_Setup)
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_element).perform()
        time.sleep(hold_time)

    def click_Seniority(self):
        self.driver.find_element(By.XPATH, self.Seniority).click()

    def click_Seniority_Add_Button(self):
        self.driver.find_element(By.XPATH, self.Seniority_Add_Button).click()

    def enter_Seniority_code(self, code):
        self.driver.find_element(By.ID, self.Seniority_Code_ID).send_keys(code)

    def enter_Seniority_From(self, From):
        self.driver.find_element(By.ID, self.Seniority_From_ID).send_keys(From)

    def enter_Seniority_To(self, To):
        self.driver.find_element(By.ID, self.Seniority_To_ID).send_keys(To)

    def click_Seniority_save(self):
        self.driver.find_element(By.XPATH, self.Seniority_save_button).click()

    def click_Seniority_action_button(self):
        self.driver.find_element(By.XPATH, self.Seniority_action_button).click()

    def click_Seniority_edit_info_button(self):
        self.driver.find_element(By.XPATH, self.Seniority_edit_info_button).click()

    def click_Seniority_update_button(self):
        self.driver.find_element(By.XPATH, self.Seniority_update_button).click()

    def click_Seniority_code_search_button(self):
        self.driver.find_element(By.XPATH, self.Seniority_code_search_button).click()

    def enter_Seniority_code_searchbar(self, code):
        self.driver.find_element(By.XPATH, self.Seniority_code_searchbar).send_keys(code)

    def click_Seniority_code_delete(self):
        self.driver.find_element(By.XPATH, self.Seniority_code_Delete).click()

    def click_Seniority_code_inactive(self):
        self.driver.find_element(By.XPATH, self.Seniority_inactive_button).click()

    def click_Seniority_code_active(self):
        self.driver.find_element(By.XPATH, self.Seniority_code_Active).click()

    def click_Seniority_code_active_button(self):
        self.driver.find_element(By.XPATH, self.Seniority_active_button).click()
