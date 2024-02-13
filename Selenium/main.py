from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/Spigen-Lithium-Polymer-Wireless-Charging/dp/B0C5D9734Q/"
           "ref=sr_1_3?keywords=spigen%2Bpower%2Bbank&sr=8-3&th=1")

price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
print(price)

# find element link by it's link text
# link = driver.find_element(By.LINK_TEXT, value="link")
# click on link
# link.click()

# find element searchbar by name
# search = driver.find_element(By.NAME, value="search")
# type into searchbar & use Key class for ENTER
# search.send_keys("Python", Keys.ENTER)

# to close active tab
# driver.close()
# to quit browser
driver.quit()
