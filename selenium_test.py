from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

driver = webdriver.Firefox()

driver.get("http://www.tennisabstract.com/charting/20221120-M-Tour_Finals-F-Novak_Djokovic-Casper_Ruud.html")

driver.find_element(By.XPATH, "//span[@id='shots1']").click()

element = driver.find_element(By.XPATH, "//table[@id='reportable']")

table = element.get_attribute('outerHTML')

df = pd.read_html(table)
df = df[0]

print(type(df))
print(df)

driver.close()