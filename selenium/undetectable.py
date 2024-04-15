from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from undetected_chromedriver.v2 import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os,time

options=webdriver.ChromeOptions()
options.add_argument("proxy-server=")
browser=Chrome(
    options=options
)

element=browser.get('https://accounts.google.com/v3/signin/identifier?ifkv=ASKXGp3dN7wn0zsWhIIyZhHbouVVCSkJBh6WARrP_eILVEBgTufFiS46rKkgL4q4lFNdOkZUahOjXA&theme=glif&flowName=GlifWebSignIn&flowEntry=ServiceLogin&continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1')

browser.find_element(By.ID,"identifierId").send_keys('akshaypiranavb@gmail.com')

browser.find_element(By.CLASS_NAME,"nCP5yc").click()

WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")))
browser.find_element(By.CLASS_NAME,"zHQkBf").send_keys('SRILATHA@AKSHAY')
browser.find_element(By.CLASS_NAME,"nCP5yc").click()
time.sleep(3600)