# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSeleniumMakeMyTrip():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_seleniumMakeMyTrip(self):
    # Test name: SeleniumMakeMyTrip
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.makemytrip.com/")
    # 2 | setWindowSize | 1835x969 | 
    self.driver.set_window_size(1835, 969)
    # 3 | click | css=.cookiesModal__acceptCookiesBtn | 
    self.driver.find_element(By.CSS_SELECTOR, ".cookiesModal__acceptCookiesBtn").click()
    # 4 | click | css=.active > .headerIconWrapper | 
    self.driver.find_element(By.CSS_SELECTOR, ".active > .headerIconWrapper").click()
    # 5 | mouseOver | linkText=Flights | 
      element = self.driver.find_element(By.LINK_TEXT, "Flights")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
    # 6 | mouseOut | linkText=Flights | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 7 | click | css=.commonModal__close | 
    self.driver.find_element(By.CSS_SELECTOR, ".commonModal__close").click()
    # 8 | click | css=li:nth-child(2) > .tabsCircle | 
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > .tabsCircle").click()
    # 9 | mouseDown | id=fromCity | 
    element = self.driver.find_element(By.ID, "fromCity")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 10 | mouseUp | css=.react-autosuggest__input | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".react-autosuggest__input")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 11 | click | css=.searchCity | 
    self.driver.find_element(By.CSS_SELECTOR, ".searchCity").click()
    # 12 | type | css=.react-autosuggest__input | hyder
    self.driver.find_element(By.CSS_SELECTOR, ".react-autosuggest__input").send_keys("hyder")
    # 13 | click | css=#react-autowhatever-1-section-0-item-0 .calc60 > .font14 | 
    self.driver.find_element(By.CSS_SELECTOR, "#react-autowhatever-1-section-0-item-0 .calc60 > .font14").click()
    # 14 | mouseDown | id=toCity | 
    element = self.driver.find_element(By.ID, "toCity")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 15 | mouseUp | css=.react-autosuggest__input | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".react-autosuggest__input")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 16 | click | css=.searchToCity | 
    self.driver.find_element(By.CSS_SELECTOR, ".searchToCity").click()
    # 17 | type | css=.react-autosuggest__input | chennai
    self.driver.find_element(By.CSS_SELECTOR, ".react-autosuggest__input").send_keys("chennai")
    # 18 | click | css=#react-autowhatever-1-section-0-item-0 .calc60 > .font14 | 
    self.driver.find_element(By.CSS_SELECTOR, "#react-autowhatever-1-section-0-item-0 .calc60 > .font14").click()
    # 19 | click | css=.activeWidget .lbl_input | 
    self.driver.find_element(By.CSS_SELECTOR, ".activeWidget .lbl_input").click()
    # 20 | click | css=.DayPicker-NavButton--next | 
    self.driver.find_element(By.CSS_SELECTOR, ".DayPicker-NavButton--next").click()
    # 21 | click | css=.DayPicker-Month:nth-child(1) .DayPicker-Week:nth-child(1) > .DayPicker-Day:nth-child(2) > .dateInnerCell | 
    self.driver.find_element(By.CSS_SELECTOR, ".DayPicker-Month:nth-child(1) .DayPicker-Week:nth-child(1) > .DayPicker-Day:nth-child(2) > .dateInnerCell").click()
    # 22 | click | css=label:nth-child(2) > .lbl_input | 
    self.driver.find_element(By.CSS_SELECTOR, "label:nth-child(2) > .lbl_input").click()
    # 23 | click | css=.DayPicker-NavButton--next | 
    self.driver.find_element(By.CSS_SELECTOR, ".DayPicker-NavButton--next").click()
    # 24 | click | css=.DayPicker-NavButton--next | 
    self.driver.find_element(By.CSS_SELECTOR, ".DayPicker-NavButton--next").click()
    # 25 | click | css=.DayPicker-Week:nth-child(5) > .DayPicker-Day--selected:nth-child(4) p | 
    self.driver.find_element(By.CSS_SELECTOR, ".DayPicker-Week:nth-child(5) > .DayPicker-Day--selected:nth-child(4) p").click()
    # 26 | click | css=.primaryBtn | 
    self.driver.find_element(By.CSS_SELECTOR, ".primaryBtn").click()
    # 27 | click | css=.overlayCrossIcon | 
    self.driver.find_element(By.CSS_SELECTOR, ".overlayCrossIcon").click()
    # 28 | click | css=div:nth-child(2) > #flightCard-0 > .listingCard > .hrtlCenter | 
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > #flightCard-0 > .listingCard > .hrtlCenter").click()
    # 29 | click | css=div:nth-child(2) > #flightCard-0 .flexOne:nth-child(3) > .blackText | 
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > #flightCard-0 .flexOne:nth-child(3) > .blackText").click()
  
