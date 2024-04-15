from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os,time
from solve import solveRecaptcha

browser=webdriver.Chrome()
element=browser.get("https://google.com/recaptcha/api2/demo")

result = solveRecaptcha(
    "6LfD3PIbAAAAAJs_eEHvoOl75_83eXSqpPSRFJ_u",
    "https://google.com/recaptcha/api2/demo"
)

print(result)