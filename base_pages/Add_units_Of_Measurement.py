from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class Add_Units_Of_Measurement_Page:
    setting_button = "//button[@aria-label='Settings']"
    Dispatch_Setup = "//span[contains(@class, 'mat-subtitle-1') and contains(text(), 'Dispatch')]"
    hover_Dispatch = "//span[contains(@class, 'sidebar-element-name') and text()='Dispatch ']"
    hover_Dispatch_Setup = "//label[contains(@class, 'sidebar-element-name') and text()='Dispatch Setup']"
    Unit_Of_Measurement = "//label[text()='Units Of Measurement ']"
    Unit_Of_Measurement_Add_Button = "//button[contains(@class, 'header_new_btn') and contains(text(), 'UOM')]"
    Unit_Of_Measurement_Name_ID = "UomName"
    Unit_Of_Measurement_Symbol_ID = "UomSymbol"
    Unit_Of_Measurement_save_button = "//button[contains(@class, 'btn-primary') and text()='Save']"
    Unit_Of_Measurement_action_button = "//mat-cell//i-tabler[@name='dots-vertical' and contains(@class, 'mat-mdc-menu-trigger')]"
    Unit_Of_Measurement_edit_info_button = "//button[.//span[text()=' Edit Info ']]"
    Unit_Of_Measurement_update_button = "//button[text()='Update' and contains(@class, 'btn-primary')]"
    Unit_Of_Measurement_code_search_button = "//label[@id='NameHeader']"
    Unit_Of_Measurement_code_searchbar = "//mat-form-field[@id='NameSearchTextBox']//input[@id='NameInputBox']"
    Unit_Of_Measurement_code_Delete = "//i-tabler[@name='logout' and contains(@class, 'action-icons')]"
    Unit_Of_Measurement_inactive_button = "//button[contains(@class, 'swal2-confirm') and contains(text(), 'Yes, Mark as Inactive!')]"
    Unit_Of_Measurement_code_Active = "//i-tabler[@name='logout-2' and contains(@class, 'action-icons')]"
    Unit_Of_Measurement_active_button = "//button[contains(@class, 'swal2-confirm') and contains(text(), 'Yes, Mark as Active!')]"

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

    def click_Unit_Of_Measurement(self):
        self.driver.find_element(By.XPATH, self.Unit_Of_Measurement).click()

    def click_Unit_Of_Measurement_Add_Button(self):
        self.driver.find_element(By.XPATH, self.Unit_Of_Measurement_Add_Button).click()

    def enter_Unit_Of_Measurement_Name(self, code):
        self.driver.find_element(By.ID, self.Unit_Of_Measurement_Name_ID).send_keys(code)

    def enter_Unit_Of_Measurement_Symbol(self, description):
        self.driver.find_element(By.ID, self.Unit_Of_Measurement_Symbol_ID).send_keys(description)

    def click_Unit_Of_Measurement_save(self):
        self.driver.find_element(By.XPATH, self.Unit_Of_Measurement_save_button).click()

    def click_Unit_Of_Measurement_action_button(self):
        self.driver.find_element(By.XPATH, self.Unit_Of_Measurement_action_button).click()

    def click_Unit_Of_Measurement_edit_info_button(self):
        self.driver.find_element(By.XPATH, self.Unit_Of_Measurement_edit_info_button).click()

    def click_Unit_Of_Measurement_update_button(self):
        self.driver.find_element(By.XPATH, self.Unit_Of_Measurement_update_button).click()

    def click_Unit_Of_Measurement_code_search_button(self):
        self.driver.find_element(By.XPATH, self.Unit_Of_Measurement_code_search_button).click()

    def enter_Unit_Of_Measurement_code_searchbar(self, code):
        self.driver.find_element(By.XPATH, self.Unit_Of_Measurement_code_searchbar).send_keys(code)

    def click_Unit_Of_Measurement_code_delete(self):
        self.driver.find_element(By.XPATH, self.Unit_Of_Measurement_code_Delete).click()

    def click_Unit_Of_Measurement_code_inactive(self):
        self.driver.find_element(By.XPATH, self.Unit_Of_Measurement_inactive_button).click()

    def click_Unit_Of_Measurement_code_active(self):
        self.driver.find_element(By.XPATH, self.Unit_Of_Measurement_code_Active).click()

    def click_Unit_Of_Measurement_code_active_button(self):
        self.driver.find_element(By.XPATH, self.Unit_Of_Measurement_active_button).click()
