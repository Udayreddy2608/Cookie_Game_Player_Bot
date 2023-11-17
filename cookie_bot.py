from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
chrome_driver_path="/Users/udayreddy/Downloads/chromedriver_mac64/chromedriver"
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)

driver.get(url="https://orteil.dashnet.org/experiments/cookie/")
cookie=driver.find_element(By.ID,value="cookie")
timeout=time.time()+5
five_min=time.time()+300
while True:
    cookie.click()
    if time.time()>timeout:
        money = driver.find_element(By.ID, value="money").text
        print(money)
        all_prices=driver.find_elements(By.CSS_SELECTOR,value="#store b")
        item_prices=[]
        item_names=[]
        for price in all_prices:
            element_text=price.text
            l=element_text.split(" - ")
            item_names.append(l[0])
            cost=l[-1].replace(",","")
            if cost!='':
                item_prices.append(int(cost))
        item_names.remove('')
        item_prices.sort(reverse=True)
        item_prices.reverse()
        for price in item_prices:
            if int(money)>price:
                ind=item_prices.index(price)
                button=item_names[ind]
                press=driver.find_element(By.ID,value=f"buy{button}")
                press.click()
    elif time.time()>five_min:
        break
cookpersec=driver.find_element(By.ID,value="cps")
print(cookpersec.text)