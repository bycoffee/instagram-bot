# Instagram Bot to Like Photos

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys
import time
from termcolor import colored, cprint


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password

		# Google Chrome
        self.driver = webdriver.Chrome('./chromedriver')
		# Firefox
        # self.driver = webdriver.Firefox('./geckodriver') 

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        cprint('\n- Opening Instagram login page...', 'yellow')
        driver.get('https://www.instagram.com/accounts/login')
        time.sleep(2)

        cprint('\n- Setting up the username', 'yellow')
        username_field = driver.find_element_by_xpath(
            "//input[@name='username']")
        username_field.clear()
        username_field.send_keys(self.username)

        cprint('- Setting up the password', 'yellow')
        password_field = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_field.clear()
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)

        time.sleep(2)

    def like(self, hashtag):
        driver = self.driver

        cprint('\n - Going to check out the #' + hashtag + ' posts', 'yellow')
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')

        cprint(' - Checking the posts on page. It can take a few seconds...', 'blue')
        time.sleep(0.5)

        # Scrolling Down
        for i in range(1, 100):
            driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(0.2)

        time.sleep(10)

        # Searching for picture link
        hrefs = driver.find_elements_by_tag_name('a')
        pic_links = []

        for elem in hrefs:

            try:
                href = elem.get_attribute('href')
                href.index('/p/')
                pic_links.append(href)
            except:
                pass

        cprint('- Photos found: ' + str(len(pic_links)), 'magenta')

        for link in pic_links:
            cprint('\n - Going to photo(url): ' + str(link), 'yellow')
            driver.get(link)

            time.sleep(1)

            time.sleep(0.1)

            like_buttons = driver.find_elements_by_css_selector(
                ".Slqrh span[aria-label='Curtir']")

            if (len(like_buttons) > 0):
                like_buttons[0].click()
                cprint('\n<3 Liked' + str(link), 'red')
            else:
                cprint('\nThere\'s no Like Button on this photo ( ' +
                       str(link) + ' )', 'grey')

            time.sleep(0.1)


cprint('\n @ INSTAGRAM BOT IN ACTION', 'magenta')
bot = InstagramBot('yourusername', 'yourpwd')
bot.login()

hashtags = ['opensource', 'code', 'violao', 'vozeviolao', 'cantando', 'paisagem', 'diy',
            'fails', 'thuglife', 'coffee', 'arduino', 'raspberry', 'programming', 'google', 'gdg']

for hashtag in hashtags:
    bot.like(hashtag)


bot.closeBrowser()
