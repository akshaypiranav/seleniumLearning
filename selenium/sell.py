from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time
os.environ["PATH"] += r"E:\selenium"

print("Initializing Chrome WebDriver...")
engine = webdriver.Chrome()
print("Chrome WebDriver initialized successfully.")
engine.get("https://www.amazon.in/s?k=mobile&crid=3BEG3HQZZ1RHO&sprefix=mobil%2Caps%2C311&ref=nb_sb_noss_2")
elem_list=engine.find_element(By.CSS_SELECTOR,"#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.s-wide-grid-style.sg-row > div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div")

# items=engine.find_elements (By.XPATH,'//*[@id="search"]')
# print("ELEMENT LIST :\n")
# print(elem_list)

# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# print(len(items))
# for i in items:
#     print("TITLE",i.text)

items = engine.find_elements(By.CSS_SELECTOR,".s-image")
for item in items:
    src_attribute = item.get_attribute("src")
    print(src_attribute)
print(len(items))

time.sleep(3600)