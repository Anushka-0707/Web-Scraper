# flip.com

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

url = 'https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url)


time.sleep(3)


titles = driver.find_elements(By.XPATH,'.//div[@class="KzDlHZ"]')
print(len(titles))
prices = driver.find_elements(By.XPATH,'.//div[@class="hl05eU"]/div[@class="Nx9bqj _4b5DiR"]')
print(len(prices))

for title , price in zip(titles,prices):
  print(f"title : {title.text} - price : {price.text}")
  
  
driver.close()