# Instagram Bot to Like Photos
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

class InstagramBot:

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.driver = webdriver.Chrome('./chromedriver')

	def closeBrowser(self):
		self.driver.close()

	def login(self):
		driver = self.driver
		driver.get('https://www.instagram.com/accounts/login')

		time.sleep(1)
		username_field = driver.find_element_by_xpath("//input[@name='username']")		
		username_field.clear()
		username_field.send_keys(self.username)

		password_field = driver.find_element_by_xpath("//input[@name='password']")
		password_field.clear()
		password_field.send_keys(self.password)
		password_field.send_keys(Keys.RETURN)

		time.sleep(1)
	
	def like(self, hashtag):
		driver = self.driver
		print('Searching for #' + hashtag + '\n\n')
		driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')

		time.sleep(0.5)

		# Scrolling Down
		for i in range (1, 100):
			driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
			time.sleep(0.2)

		print('Please, just wait a little...')
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
		
		print(str(len(pic_links)) + ' photos found!\nLet\'s start liking...\n\n')

		for link in pic_links:
			print('Going to photo: ' + str(link))
			driver.get(link)

			like_button = driver.find_element_by_css_selector(".Slqrh span[aria-label='Like']")
			time.sleep(0.1)
			like_button.click()

			time.sleep(0.1)
				

bot = InstagramBot('your_username', 'your_password')
bot.login()

hashtags = ['your', 'hash', 'tags', 'here']

for hashtag in hashtags:
	bot.like(hashtag)

bot.closeBrowser()