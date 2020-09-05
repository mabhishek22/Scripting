from selenium import webdriver
from getpass import getpass

# usr = input('Enter the credentials\n')
# pwd = getpass('enter password')

driver = webdriver.Firefox()
driver.get('https://www.facebook.com/')

username_text = driver.find_element_by_id('email')
username_text.send_keys(usr)

password_text = driver.find_element_by_id('pass')
password_text.send_keys(pwd)


login = driver.find_element_by_id('u_0_2')
login.submit()
