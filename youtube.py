from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.options import options

#chromeOptions = Options()
#chromeOptions.add_argument("--incognito")
#driver = webdriver.Chrome(ChromDriveManager().install(), options = chromeOptions)
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.youtube.com/")

searchBox = driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input")
searchBox.send_keys("sloth")

searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()
