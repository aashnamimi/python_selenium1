import pytest
from selenium import webdriver
import time
import Pages.Drivers
from Pages import Drivers
from Workflows import HomePage_search



@pytest.fixture()
def test_setup():
    global driver   
    driver = webdriver.Chrome(executable_path=Pages.Drivers.Drivers.CHROME_EXECUTABLE_PATH)   
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield    
    driver.close()
    driver.quit()    
    print("test complete")


def test_login_valid(test_setup):
    driver.get(Pages.Drivers.Drivers.BASE_URL)
    time.sleep(5) 
     
    # hp=HomePage_search.HomePage_search(driver) 
    homePage=HomePage_search.HomePage_search(driver)
    homePage.enter_username("Admin")
    homePage.enter_password("admin123")
    # login = Pages.x_paths.Locators(driver)
    
    
