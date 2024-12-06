from selenium.webdriver.common.by import By


class Login_Admin_Page:
    textbox_username_id = "uname"
    textbox_password_id = "password"
    btn_login_class = "mdc-button__label"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CLASS_NAME, self.btn_login_class).click()
