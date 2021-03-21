from selenium import webdriver
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
        time.sleep(3)
        BuyGPU.click()
        Available = True
travis.get("https://www.bestbuy.com/cart")
GoToCart = travis.find_element_by_class_name("btn-primary")
GoToCart.click()
travis.get("https://www.bestbuy.com/identity/signin?token=tid%3A256344d2-8a88-11eb-9fba-005056aeda70")
GoAsGuest = travis.find_element_by_class_name("btn-lg")
GoAsGuest.click()



