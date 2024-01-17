import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.set_window_size(1835, 969)
    driver.implicitly_wait(10)
    yield driver
    # driver.quit()


def test_makemytrip(driver):
    driver.get("https://www.makemytrip.com/")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".cookiesModal__acceptCookiesBtn").click()
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

    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "datePickerContainer").click()
    driver.find_element(By.XPATH, "//span[@aria-label='Next Month']").click()
    driver.find_element(By.XPATH, "//p[text()='19']").click()

    driver.find_element(By.XPATH, "//span[@aria-label='Next Month']").click()
    driver.find_element(By.XPATH, "//span[@aria-label='Next Month']").click()
    driver.find_element(By.XPATH, "//p[text()='19']").click()

    driver.find_element(By.XPATH, "//a[text()='Search']").click()

    time.sleep(3)
    # driver.find_element(By.XPATH,"//*[contains(text(),'GO BACK TO HOMEPAGE')]").click()

    # elem = driver.find_element(By.XPATH, "//button[text()='Book Now']").size
    print(driver.current_url)
    # print(elem.is_displayed())
    #  assert driver.find_element(By.XPATH,
    #                            "//button[text()='Book Now']").is_displayed(), "No such element error displayed"
    # assertTrue(driver.find_element(By.XPATH, "//button[text()='Book Now']").is_displayed(), "assertion")
    assert "Book Now" in driver.page_source
    # assert "GO BACK TO HOMEPAGE" in driver.page_source
    time.sleep(10)
