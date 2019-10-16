from selenium import webdriver
from selenium.webdriver.common.by import By

class Locators():  
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, "txtUsername")
        self.password_textbox=(By.ID,"txtPassword")
        self.login_button=(By.ID,"btnLogin")
        self.username_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"        
