from selenium import webdriver

import os,time

from selenium.webdriver.common.by import By


browser=webdriver.Chrome()
print("Chrome WebDriver initialized successfully.")
browser.get("https://www.amazon.in/s?k=mobile&crid=REWM50K3RUC3&sprefix=%2Caps%2C293&ref=nb_sb_ss_recent_1_0_recent")

element=browser.find_element(By.CSS_SELECTOR,'div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16')

items=element.find_elements(By.XPATH,'//div[@data-component-type="s-search-result"]')

print(len(items))
for item in items:
    price=item.find_element(By.CLASS_NAME,"a-price-whole").text
    title=item.find_element(By.TAG_NAME,'h2').text
    image=item.find_element(By.CLASS_NAME,'s-image').get_attribute("src")
    image_url=item.find_element(By.CLASS_NAME,'a-link-normal').get_attribute("href")
    print("Title",title,"Price",price,"IMAGE URL",image,"\n","Image Url",image_url)    

