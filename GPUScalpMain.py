from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

###Location of webdriver.exe
PATH = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"
###URL to download chrome driver
###(https://sites.google.com/a/chromium.org/chromedriver/downloads)
travis = webdriver.Chrome(PATH)

#travis.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442")
###Test Study
travis.get("https://www.bestbuy.com/site/pny-geforce-gt1030-2gb-pci-e-3-0-graphics-card-black/5901353.p?skuId=5901353")
Available = False
OutOfStock = True

while(Available != True):
    try:
        BuyGPU = travis.find_element_by_class_name("btn-disabled")
        print(travis.title)
        print("Out of Stock")
        time.sleep(2)
        travis.refresh()
    except:
        BuyGPU = travis.find_element_by_class_name("btn-primary")
        print(travis.title)
        print("In Stock Purchasing")
        time.sleep(2)
        BuyGPU.click()
        Available = True

Cart = travis.get("https://www.bestbuy.com/cart")
GoToCheckout = travis.find_element_by_class_name("btn-primary").click()

try:
    LoginPage = WebDriverWait(travis, 10).until(
        EC.presence_of_element_located((By.ID, "fld-e"))
    )
    usrnme = travis.find_element_by_id("fld-e")
    usrnme.send_keys("getscammed42069@gmail.com")
    psswrd = travis.find_element_by_id("fld-p1")
    psswrd.send_keys("Doublebub@21")
    SignIn = travis.find_element_by_class_name("btn-secondary").click()
    time.sleep(3)
    ContToPayment = travis.find_element_by_class_name("btn-secondary").click()
    try:
        LoginPage = WebDriverWait(travis, 10).until(
            EC.presence_of_element_located((By.ID, "optimized-cc-card-number"))
        )
        card = travis.find_elements_by_id("optimized-cc-card-number").send_keys("4829512674")
        firstname = travis.find_element_by_id("payment.billingAddress.firstName").send_keys("Travis")
        lastname = travis.find_element_by_id("payment.billingAddress.lastName").send_keys("Dingleberry")
        address = travis.find_element_by_id("payment.billingAddress.street").send_keys("1125 West Grove ST")
    except:
        print("Issue with Payment")
        travis.quit()
except:
    print("Error on Login")
    travis.quit()






