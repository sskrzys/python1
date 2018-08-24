from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
browser.get("www.facebook.com")

username = browser.find_element_by_id("guru99")
password = browser.find_element_by_id("password@123")
submit = browser.find_element_by_id("submit")

username.send_keys("me")
password.send_keys("mykewlpass")

submit.click()

wait = WebDriverWait(browser, 5)

try:
    page_loaded = wait.until_not(
        lambda browser: browser.current_url == "login_page"
    )
except TimeoutException:
    self.fail("Loading timeout expired")
    self.assertEqual(
        browser.current_url,
        correct_page,
        msg="Successful Login"
    )