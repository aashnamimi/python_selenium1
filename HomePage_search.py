# from Pages import Generic_Methods
from Pages import x_paths

# class HomePage_search(Generic_Methods):
class HomePage_search(x_paths.Locators):
   
    # locators=Pages.x_paths.Locators(driver)
   

    def __init__(self, driver):
        
        super().__init__(driver)
        
    
    def enter_username(self,username):                
        # locators.username_textbox(username)
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)
        # self.driver.find_element(self.username_textbox).send_keys(username)
        
        # self.driver.find_element(x_paths.Locators.username_textbox).send_keys(username)
        # self.username_textbox.send_keys(username)
        
    def enter_password(self,password):
        # self.password_textbox.send_keys(password)
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
    def click_login(self):
        
        # self.driver.find_element_by_id(self.login_button_id).click()
        self.driver.find_element_by_id(self.login_button_id).click()
