from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('https://google.com')

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("Anh Nguyen")
elem.send_keys(Keys.RETURN)