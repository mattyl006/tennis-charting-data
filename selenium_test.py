from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.tennisabstract.com/charting/20221120-M-Tour_Finals-F-Novak_Djokovic-Casper_Ruud.html")

driver.find_element_by_css_selector('.shots1.rounds').click()

driver.close()