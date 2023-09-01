from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com.tr/?hl=tr")
input = driver.find_element(By.NAME,"q")
input.send_keys("kodlama.io")
searchButton = driver.find_element(By.NAME,"btnK")
sleep(2)

searchButton.click()
sleep(3)

firstResult = driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/a")
firstResult.click()
listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlama.io sitesinde {len(listOfCourses)} adet kurs var.")
while True:
    continue


# HTML LOCATORS
# Web scraping
# Data scraping

#Full xpath
# /html/body/div[6]/div/div[9]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/a

# Xpath
# //*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/a

