from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "your_email@example.com"
TWITTER_PASSWORD = "your_password"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        time.sleep(60)
        self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(3)
        email_input = self.driver.find_element(By.NAME, "text")
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.ENTER)
        time.sleep(3)
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_box = self.driver.find_element(By.CSS_SELECTOR, "br[data-text='true']")
        tweet_box.send_keys(tweet)
        tweet_box.send_keys(Keys.COMMAND, Keys.ENTER)

    def quit(self):
        self.driver.quit()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
bot.quit()