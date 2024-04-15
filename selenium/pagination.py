from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os,time,json


def writeJson(new_data, filename='data.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)

        file_data.append(new_data)

        file.seek(0)

        json.dump(file_data, file, indent = 4)

browser=webdriver.Chrome()
elements=browser.get("https://www.amazon.in/s?k=hammer&crid=2WWQYIY7ECD4J&sprefix=hamme%2Caps%2C298&ref=nb_sb_noss_2")
isnotvalue=False

while not isnotvalue:
    try:
        elementwait=WebDriverWait(browser, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//div[@data-component-type="s-search-result"]')))
        element=browser.find_element(By.CSS_SELECTOR,'div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16')

        value=element.find_elements(By.XPATH,'//div[@data-component-type="s-search-result"]')
        for item in value:
            price=item.find_element(By.CLASS_NAME,"a-price-whole").text
            title=item.find_element(By.TAG_NAME,'h2').text
            image=item.find_element(By.CLASS_NAME,'s-image').get_attribute("src")
            image_url=item.find_element(By.CLASS_NAME,'a-link-normal').get_attribute("href")
            print("Title",title,"Price",price,"IMAGE URL",image,"\n","Image Url",image_url)
            writeJson({
                "title": title,

            })    
        
        try:
            print("TRYING TO DO")
            nextbtn = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 's-pagination-next')))

            next=nextbtn.get_attribute('class')
            if "disabled" in next:
                isnotvalue=True
            else:
                browser.find_element(By.CLASS_NAME,"s-pagination-next").click()

        except Exception as e:
            print("ERROR",e)

    except:
        print("ERROR")
        isnotvalue=True
        