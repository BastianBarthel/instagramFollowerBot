import os
import time
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

CHROME_DRIVER_PATH = "/Applications/chromedriver"
SIMILAR_ACCOUNT = "https://www.instagram.com/sallysbakeblog/"
INSTAGRAM_EMAIL = os.environ.get(INSTAGRAM_EMAIL)
INSTAGRAM_PASSWORD = os.environ.get(INSTAGRAM_PASSWORD)


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        accept_cookies = self.driver.find_element_by_css_selector(".bIiDR  ")
        accept_cookies.click()
        username = self.driver.find_element_by_name("username")
        username.send_keys(INSTAGRAM_EMAIL)
        password = self.driver.find_element_by_name("password")
        password.send_keys(INSTAGRAM_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(6)

    def find_followers(self):
        self.driver.get(SIMILAR_ACCOUNT)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for n in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements_by_css_selector(".PZuss button")
        for button in range(len(follow_buttons)-1):
            try:
                follow_buttons[button].click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
