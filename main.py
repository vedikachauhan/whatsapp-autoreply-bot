from customer import Customer
from watcher import Watcher
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
input("Press enter when you have logged in")

customer1 = Customer(driver)
customer2 = Customer(driver)

customer1.name = "MayTan"
customer2.name = "Mommy "

watcher = Watcher()

watcher.customers = [customer1, customer2]
while True:
    print("watching for new messages")
    watcher.check_new_message()
    time.sleep(60)
