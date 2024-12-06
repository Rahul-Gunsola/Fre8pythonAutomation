from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class Add_Carrier_Type_Page:
    setting_button = "//button[@aria-label='Settings']"
    Dispatch_Setup = "//span[contains(@class, 'mat-subtitle-1') and contains(text(), 'Dispatch')]"
    hover_Dispatch = "//span[contains(@class, 'sidebar-element-name') and text()='Dispatch ']"
    hover_Dispatch_Setup = "//label[contains(@class, 'sidebar-element-name') and text()='Dispatch Setup']"
    Carrier_Type = "//label[contains(@class, 'hide-menu') and text()='Carrier Types ']"
    Carrier_Type_Add_Button = "//button[contains(@class, 'header_new_btn') and contains(text(), 'Type')]"
    Carrier_Type_Code_ID = "carrierCode"
    Carrier_Type_DES_ID = "description"
    Carrier_Type_save_button = "//button[contains(@class, 'btn-primary') and text()='Save']"
    Carrier_Type_action_button = "//mat-cell//i-tabler[@name='dots-vertical' and contains(@class, 'mat-mdc-menu-trigger')]"
    Carrier_Type_edit_info_button = "//button[.//span[text()=' Edit Info ']]"
    Carrier_Type_update_button = "//button[text()='Update' and contains(@class, 'btn-primary')]"
    Carrier_Type_code_search_button = "//label[@id='NameHeader']"
    Carrier_Type_code_searchbar = "//mat-form-field[@id='NameSearchTextBox']//input[@id='NameInputBox']"
    Carrier_Type_code_Delete = "//i-tabler[@name='logout' and contains(@class, 'action-icons')]"
    Carrier_Type_inactive_button = "//button[contains(@class, 'swal2-confirm') and contains(text(), 'Yes, Mark as Inactive!')]"
    Carrier_Type_code_Active = "//i-tabler[@name='logout-2' and contains(@class, 'action-icons')]"
    Carrier_Type_active_button = "//button[contains(@class, 'swal2-confirm') and contains(text(), 'Yes, Mark as Active!')]"

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

    def click_Carrier_Type(self):
        self.driver.find_element(By.XPATH, self.Carrier_Type).click()

    def click_Carrier_Type_Add_Button(self):
        self.driver.find_element(By.XPATH, self.Carrier_Type_Add_Button).click()

    def enter_Carrier_Type_code(self, code):
        self.driver.find_element(By.ID, self.Carrier_Type_Code_ID).send_keys(code)

    def enter_Carrier_Type_des(self, description):
        self.driver.find_element(By.ID, self.Carrier_Type_DES_ID).send_keys(description)

    def click_Carrier_Type_save(self):
        self.driver.find_element(By.XPATH, self.Carrier_Type_save_button).click()

    def click_Carrier_Type_action_button(self):
        self.driver.find_element(By.XPATH, self.Carrier_Type_action_button).click()

    def click_Carrier_Type_edit_info_button(self):
        self.driver.find_element(By.XPATH, self.Carrier_Type_edit_info_button).click()

    def click_Carrier_Type_update_button(self):
        self.driver.find_element(By.XPATH, self.Carrier_Type_update_button).click()

    def click_Carrier_Type_code_search_button(self):
        self.driver.find_element(By.XPATH, self.Carrier_Type_code_search_button).click()

    def enter_Carrier_Type_code_searchbar(self, code):
        self.driver.find_element(By.XPATH, self.Carrier_Type_code_searchbar).send_keys(code)

    def click_Carrier_Type_code_delete(self):
        self.driver.find_element(By.XPATH, self.Carrier_Type_code_Delete).click()

    def click_Carrier_Type_code_inactive(self):
        self.driver.find_element(By.XPATH, self.Carrier_Type_inactive_button).click()

    def click_Carrier_Type_code_active(self):
        self.driver.find_element(By.XPATH, self.Carrier_Type_code_Active).click()

    def click_Carrier_Type_code_active_button(self):
        self.driver.find_element(By.XPATH, self.Carrier_Type_active_button).click()
