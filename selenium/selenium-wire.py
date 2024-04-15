from seleniumwire import webdriver  # Import from seleniumwire
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Go to the Google home page

for i in range(1, 61):
    if i < 10:
        driver.get(f"https://erp.kamarajengg.edu.in/parent/ERP/student/images/student/21UAD00{i}.jpg")
    else:
        driver.get(f"https://erp.kamarajengg.edu.in/parent/ERP/student/images/student/21UBT0{i}.jpg")

    time.sleep(1)

# Close the browser after all iterations
driver.quit()
