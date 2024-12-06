from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class Add_Loyalty_Page:
    setting_button = "//button[@aria-label='Settings']"
    Dispatch_Setup = "//span[contains(@class, 'mat-subtitle-1') and contains(text(), 'Dispatch')]"
    hover_Dispatch = "//span[contains(@class, 'sidebar-element-name') and text()='Dispatch ']"
    hover_Dispatch_Setup = "//label[contains(@class, 'sidebar-element-name') and text()='Dispatch Setup']"
    Loyalty = "//label[contains(@class, 'hide-menu sidebar-element-name') and text()='Loyalty Codes ']"
    Loyalty_Add_Button = "//button[contains(@class, 'header_new_btn') and contains(text(), 'Loyalty')]"
    Loyalty_Code_ID = "loyaltyCode"
    Loyalty_From_ID = "fromYear"
    Loyalty_To_ID = "toYear"
    Loyalty_save_button = "//button[contains(@class, 'btn-primary') and text()='Save']"
    Loyalty_action_button = "//mat-cell//i-tabler[@name='dots-vertical' and contains(@class, 'mat-mdc-menu-trigger')]"
    Loyalty_edit_info_button = "//button[.//span[text()=' Edit Info ']]"
    Loyalty_update_button = "//button[text()='Update' and contains(@class, 'btn-primary')]"
    Loyalty_code_search_button = "//label[@id='NameHeader']"
    Loyalty_code_searchbar = "//mat-form-field[@id='NameSearchTextBox']//input[@id='NameInputBox']"
    Loyalty_code_Delete = "//i-tabler[@name='logout' and contains(@class, 'action-icons')]"
    Loyalty_inactive_button = "//button[contains(@class, 'swal2-confirm') and contains(text(), 'Yes, Mark as Inactive!')]"
    Loyalty_code_Active = "//i-tabler[@name='logout-2' and contains(@class, 'action-icons')]"
    Loyalty_active_button = "//button[contains(@class, 'swal2-confirm') and contains(text(), 'Yes, Mark as Active!')]"

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

    def click_Loyalty(self):
        self.driver.find_element(By.XPATH, self.Loyalty).click()

    def click_Loyalty_Add_Button(self):
        self.driver.find_element(By.XPATH, self.Loyalty_Add_Button).click()

    def enter_Loyalty_code(self, code):
        self.driver.find_element(By.ID, self.Loyalty_Code_ID).send_keys(code)

    def enter_Loyalty_From(self, From):
        self.driver.find_element(By.ID, self.Loyalty_From_ID).send_keys(From)

    def enter_Loyalty_To(self, To):
        self.driver.find_element(By.ID, self.Loyalty_To_ID).send_keys(To)

    def click_Loyalty_save(self):
        self.driver.find_element(By.XPATH, self.Loyalty_save_button).click()

    def click_Loyalty_action_button(self):
        self.driver.find_element(By.XPATH, self.Loyalty_action_button).click()

    def click_Loyalty_edit_info_button(self):
        self.driver.find_element(By.XPATH, self.Loyalty_edit_info_button).click()

    def click_Loyalty_update_button(self):
        self.driver.find_element(By.XPATH, self.Loyalty_update_button).click()

    def click_Loyalty_code_search_button(self):
        self.driver.find_element(By.XPATH, self.Loyalty_code_search_button).click()

    def enter_Loyalty_code_searchbar(self, code):
        self.driver.find_element(By.XPATH, self.Loyalty_code_searchbar).send_keys(code)

    def click_Loyalty_code_delete(self):
        self.driver.find_element(By.XPATH, self.Loyalty_code_Delete).click()

    def click_Loyalty_code_inactive(self):
        self.driver.find_element(By.XPATH, self.Loyalty_inactive_button).click()

    def click_Loyalty_code_active(self):
        self.driver.find_element(By.XPATH, self.Loyalty_code_Active).click()

    def click_Loyalty_code_active_button(self):
        self.driver.find_element(By.XPATH, self.Loyalty_active_button).click()
