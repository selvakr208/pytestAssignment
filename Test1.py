import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.set_window_size(1835, 969)
driver.get("https://www.makemytrip.com/")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".cookiesModal__acceptCookiesBtn").click()
# driver.find_element(By.CSS_SELECTOR, ".active > .headerIconWrapper").click()
driver.find_element(By.XPATH, "//span[text()='Flights']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[text()='Round Trip']").click()
driver.find_element(By.ID, "fromCity").click()
driver.find_element(By.CSS_SELECTOR, ".searchCity").click()
driver.find_element(By.CSS_SELECTOR, ".react-autosuggest__input").send_keys("hyder")
driver.find_element(By.XPATH, "//p[text()='Hyderabad, India']").click()

driver.find_element(By.ID, "toCity").click()
driver.find_element(By.CSS_SELECTOR, ".searchToCity").click()
driver.find_element(By.CSS_SELECTOR, ".react-autosuggest__input").send_keys("chennai")
driver.find_element(By.XPATH, "//p[text()='Chennai, India']").click()

# driver.find_element(By.CSS_SELECTOR, ".activeWidget .lbl_input").click()
# driver.find_element(By.CSS_SELECTOR, ".DayPicker-NavButton--next").click()
# driver.find_element(By.XPATH, "//*[text()='Round Trip']").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME,"datePickerContainer").click()
# driver.find_element(By.ID,"departure").click()
driver.find_element(By.XPATH,"//span[@aria-label='Next Month']").click()
driver.find_element(By.XPATH,"//p[text()='19']").click()

# element = driver.find_element(By.XPATH, "//div[text()='February']/ancestor::div[@class='DayPicker-Month']")
# element.find_element(By.XPATH,
#                      "//p[text()='16']/ancestor::div[@class='DayPicker-Day' and @aria-selected='false']").click()

driver.find_element(By.XPATH,"//span[@aria-label='Next Month']").click()
driver.find_element(By.XPATH,"//span[@aria-label='Next Month']").click()
driver.find_element(By.XPATH,"//p[text()='19']").click()

driver.find_element(By.XPATH,"//a[text()='Search']").click()
# element = driver.find_element(By.LINK_TEXT, "Flights")
# actions = ActionChains(driver)
# actions.move_to_element(element).perform()
# driver.find_element(By.XPATH,"//button[text()='OKAY, GOT IT!']").click()
time.sleep(3)
# elem = driver.find_element(By.XPATH,"//button[text()='Book Now']")

# print(elem.is_displayed())
assert driver.find_element(By.XPATH, "//button[text()='Book Now']").size, 1

time.sleep(5)
driver.close()
driver.quit()
print('Done')
