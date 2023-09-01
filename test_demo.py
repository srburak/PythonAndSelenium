from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

class Test_Demo:

    # Her test öncesi çağırılır
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
    # Her test sonrası çağırılır
    def teardown_method(self):
        self.driver.quit()
    # setup -> test_demo -> teardown
    def test_demo(self):
        text = "Hello"
        assert text == "Hello"
    # setup -> test_demo2 -> teardown
    def test_demo2(self):
        assert True

    def test_invalit_login(self):
         # En fazla 5 saniye olacak şeklide user-name id'li elementin görünmesini bekle 
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        usernameInput = self.driver.find_element(By.ID , "user-name")
        # En fazla 5 saniye olacak şeklide password id'li elementin görünmesini bekle 
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID , "password")
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMesage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMesage.text == "Epic sadface: Username and password do not match any user in this service"