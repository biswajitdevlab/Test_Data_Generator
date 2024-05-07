from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.by import By

# Read data from CSV file
data = pd.read_csv('test_data.csv')

# Initialize Chrome WebDriver
driver = webdriver.Chrome()
count=0
# Iterate over each row in the DataFrame
for index, row in data.iterrows():
    count+=1
    # Get email and password from the current row
    email = row['Email']
    password = row['Password']

    # Open Facebook login page
    driver.get('https://www.facebook.com')
    driver.implicitly_wait(10)

    # Enter email and password
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "pass").send_keys(password)

    # Click on the login button
    driver.find_element(By.NAME, "login").click()

    sleep(2)
    print("Successfully Executed With",'Data: ',count)
# Close the browser window
driver.quit()
