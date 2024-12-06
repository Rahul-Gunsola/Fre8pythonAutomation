from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class Add_Indirect_Cost_matrix_Page:
    setting_button = "//button[@aria-label='Settings']"
    Dispatch_Setup = "//span[contains(@class, 'mat-subtitle-1') and contains(text(), 'Dispatch')]"
    hover_Dispatch = "//span[contains(@class, 'sidebar-element-name') and text()='Dispatch ']"
    hover_Dispatch_Setup = "//label[contains(@class, 'sidebar-element-name') and text()='Dispatch Setup']"
    Indirect_Cost_matrix = "//label[text()='Indirect Cost Matrix ']"
    Indirect_Cost_matrix_Add_Button = "//button[contains(@class, 'header_new_btn') and contains(text(), ' Indirect Cost Matrix')]"
    Indirect_Cost_matrix_Number_ID = "MatrixNumber"
    Indirect_Cost_matrix_Name_ID = "MatrixName"
    Indirect_Cost_matrix_Currency_ID = "Currency"
    # #Indirect_Cost_matrix_Currency_text = "//div[@role='option']//span[contains(text(), 'NAD - Dollars')]"
    Indirect_Cost_matrix_Description_ID = "Description-0"
    Indirect_Cost_matrix_Calculate_By_ID = "CalculatedBy-0"
    Indirect_Cost_matrix_Highway_Rate_ID = "HighwayRate-0"
    Indirect_Cost_matrix_Local_Rate_ID = "LocalRate-0"
    Indirect_Cost_matrix_save_button_ID = "headerSaveBtn"
    Indirect_Cost_matrix_action_button = "//mat-cell//i-tabler[@name='dots-vertical' and contains(@class, 'mat-mdc-menu-trigger')]"
    Indirect_Cost_matrix_edit_info_button = "//button[.//span[text()=' Edit Info ']]"
    Indirect_Cost_matrix_update_button_ID = "headerSaveBtn"
    Indirect_Cost_matrix_code_search_button = "//label[@id='MatrixNumberHeader']"
    Indirect_Cost_matrix_code_searchbar = "//mat-form-field[@id='MatrixNumberSearchTextBox']//input[@id='MatrixNumberInputBox']"
    Indirect_Cost_matrix_code_Delete = "//i-tabler[@name='logout' and contains(@class, 'action-icons')]"
    Indirect_Cost_matrix_inactive_button = "//button[contains(@class, 'swal2-confirm') and contains(text(), 'Yes, Mark as Inactive!')]"
    Indirect_Cost_matrix_code_Active = "//i-tabler[@name='logout-2' and contains(@class, 'action-icons')]"
    Indirect_Cost_matrix_active_button = "//button[contains(@class, 'swal2-confirm') and contains(text(), 'Yes, Mark as Active!')]"

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

    def click_Indirect_Cost_matrix(self):
        self.driver.find_element(By.XPATH, self.Indirect_Cost_matrix).click()

    def click_Indirect_Cost_matrix_Add_Button(self):
        self.driver.find_element(By.XPATH, self.Indirect_Cost_matrix_Add_Button).click()

    def enter_Indirect_Cost_matrix_number(self, number):
        self.driver.find_element(By.ID, self.Indirect_Cost_matrix_Number_ID).send_keys(number)

    def enter_Indirect_Cost_matrix_name(self, name):
        self.driver.find_element(By.ID, self.Indirect_Cost_matrix_Name_ID).send_keys(name)

    def click_Indirect_Cost_matrix_currency(self):
        self.driver.find_element(By.ID, self.Indirect_Cost_matrix_Currency_ID).click()

    def enter_Indirect_Cost_matrix_description(self, description):
        self.driver.find_element(By.ID, self.Indirect_Cost_matrix_Description_ID).send_keys(description)

    def click_Indirect_Cost_matrix_calculate_by(self):
        self.driver.find_element(By.ID, self.Indirect_Cost_matrix_Calculate_By_ID).click()

    def enter_Indirect_Cost_matrix_highway_rate(self, highway_rate):
        self.driver.find_element(By.ID, self.Indirect_Cost_matrix_Highway_Rate_ID).send_keys(highway_rate)

    def enter_Indirect_Cost_matrix_local_rate(self, local_rate):
        self.driver.find_element(By.ID, self.Indirect_Cost_matrix_Local_Rate_ID).send_keys(local_rate)

    def click_Indirect_Cost_matrix_save(self):
        self.driver.find_element(By.ID, self.Indirect_Cost_matrix_save_button_ID).click()

    def click_Indirect_Cost_matrix_action_button(self):
        self.driver.find_element(By.XPATH, self.Indirect_Cost_matrix_action_button).click()

    def click_Indirect_Cost_matrix_edit_info_button(self):
        self.driver.find_element(By.XPATH, self.Indirect_Cost_matrix_edit_info_button).click()

    def click_Indirect_Cost_matrix_update_button(self):
        self.driver.find_element(By.ID, self.Indirect_Cost_matrix_update_button_ID).click()

    def click_Indirect_Cost_matrix_code_search_button(self):
        self.driver.find_element(By.XPATH, self.Indirect_Cost_matrix_code_search_button).click()

    def enter_Indirect_Cost_matrix_code_searchbar(self, code):
        self.driver.find_element(By.XPATH, self.Indirect_Cost_matrix_code_searchbar).send_keys(code)

    def click_Indirect_Cost_matrix_code_delete(self):
        self.driver.find_element(By.XPATH, self.Indirect_Cost_matrix_code_Delete).click()

    def click_Indirect_Cost_matrix_code_inactive(self):
        self.driver.find_element(By.XPATH, self.Indirect_Cost_matrix_inactive_button).click()

    def click_Indirect_Cost_matrix_code_active(self):
        self.driver.find_element(By.XPATH, self.Indirect_Cost_matrix_code_Active).click()

    def click_Indirect_Cost_matrix_code_active_button(self):
        self.driver.find_element(By.XPATH, self.Indirect_Cost_matrix_active_button).click()
