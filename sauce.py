from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import globalConstants

class Test_Sauce:

    def test_invalid_loding(self):
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
        testResult = errorMesage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU : {testResult}")

    def test_valit_login(self):
        self.driver.get(globalConstants.URL)
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        usernameInput = self.driver.find_element(By.ID , "user-name")
        # En fazla 5 saniye olacak şeklide password id'li elementin görünmesini bekle 
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID , "password")
        # action chains
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        #usernameInput.send_keys("standard_user")
        #passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.driver.execute_script("window.scrollTo(0,500)")



testClass = Test_Sauce()
testClass.test_invalid_loding()
testClass.test_valit_login()
