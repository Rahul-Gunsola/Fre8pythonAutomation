from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
class Add_Department_Page:

    setting_button = "//button[@aria-label='Settings']"
    Organization = "//span[text()=' Organization ']"
    hover_Organization = "//app-nav-item//span[contains(@class, 'sidebar-element-name') and contains(text(), 'Organization')]"
    Department = "//label[contains(@class, 'hide-menu sidebar-element-name') and contains(text(), 'Departments')]"
    Department_Add_Button = "//button[contains(@class, 'header_new_btn') and contains(text(), 'Department')]"
    Department_Code_ID = "DepartmentCode"
    Department_DES_ID = "Description"
    Department_save_button = "//button[contains(@class, 'btn-primary') and text()='Save']"
    Department_action_button = "//mat-cell//i-tabler[@name='dots-vertical' and contains(@class, 'mat-mdc-menu-trigger')]"
    Department_edit_info_button = "//button[.//span[text()=' Edit Info ']]"
    Department_update_button = "//button[text()='Update' and contains(@class, 'btn-primary')]"
    Department_code_search_button = "//label[@id='NameHeader' and text()=' Department Code']"
    Department_code_searchbar = "//mat-form-field[@id='NameSearchTextBox']//input[@id='NameInputBox']"
    Department_code_Delete = "//i-tabler[@name='logout' and contains(@class, 'action-icons')]"
    Department_inactive_button = "//button[contains(@class, 'swal2-confirm') and contains(text(), 'Yes, Mark as Inactive!')]"
    Department_code_Active = "//i-tabler[@name='logout-2' and contains(@class, 'action-icons')]"
    Department_active_button = "//button[contains(@class, 'swal2-confirm') and contains(text(), 'Yes, Mark as Active!')]"

    def __init__(self, driver):
        self.driver = driver

    def click_setting(self):
        # Click on the settings button
        self.driver.find_element(By.XPATH, self.setting_button).click()

    def click_Organization(self):
        # Click on the organization menu
        self.driver.find_element(By.XPATH, self.Organization).click()

    def hover_organization(self, hold_time=5):
        # Hover over the organization sidebar menu
        hover_element = self.driver.find_element(By.XPATH, self.hover_Organization)
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_element).perform()
        time.sleep(hold_time)


    def click_department(self):
        self.driver.find_element(By.XPATH, self.Department).click()

    def click_department_Add_Button(self):
        self.driver.find_element(By.XPATH, self.Department_Add_Button).click()

    def enter_department_code(self, code):
        self.driver.find_element(By.ID, self.Department_Code_ID).send_keys(code)

    def enter_department_des(self, description):
        self.driver.find_element(By.ID, self.Department_DES_ID).send_keys(description)

    def click_department_save(self):
        self.driver.find_element(By.XPATH, self.Department_save_button).click()

    def click_department_action_button(self):
        self.driver.find_element(By.XPATH, self.Department_action_button).click()

    def click_department_edit_info_button(self):
        self.driver.find_element(By.XPATH, self.Department_edit_info_button).click()

    def click_department_update_button(self):
        self.driver.find_element(By.XPATH, self.Department_update_button).click()

    def click_department_code_search_button(self):
        self.driver.find_element(By.XPATH, self.Department_code_search_button).click()

    def enter_department_code_searchbar(self, code):
        self.driver.find_element(By.XPATH, self.Department_code_searchbar).send_keys(code)

    def click_department_code_delete(self):
        self.driver.find_element(By.XPATH, self.Department_code_Delete).click()

    def click_department_code_inactive(self):
        self.driver.find_element(By.XPATH, self.Department_inactive_button).click()

    def click_department_code_active(self):
        self.driver.find_element(By.XPATH, self.Department_code_Active).click()

    def click_department_code_active_button(self):
        self.driver.find_element(By.XPATH, self.Department_active_button).click()