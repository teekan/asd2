from selenium import webdriver
import time
import os
import subprocess
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.headless = True
path = os.getcwd()+"/geckodriver"
def hit():
	# Open browser
	print("Browser")
	driver = webdriver.Firefox(options=opts,executable_path=path)
	print(driver)

	# Load Page
	print("Page")
	driver.get("http://www.slutbags.tk")
	print(driver)

	print("Tabs so far")
	print(driver.window_handles)

	# Find popunder element
	body = driver.find_elements_by_class_name("text-center")
	print(body)
	body[0].click()

	print("Tabs so far... thus")
	print(driver.window_handles)

	# Switch window back to home page
	print("Switching from " + driver.title + " to ")
	driver.switch_to.window(driver.window_handles[1])
	print(driver.title)

	# Get Ad element
	ads = driver.find_elements_by_tag_name("iframe")
	print(ads)

	# Click ad elemement
	ads[0].click()

	# Wrapping Up
	print("All tab after process")
	print(driver.window_handles)

	# Closing tabs
	print("Closing tabs...")
	for tab in driver.window_handles:
		driver.switch_to.window(tab)
		print("Closing " + driver.title)
		driver.close()

	subprocess.run(['sudo','./delete-profiles.sh'])

while True:
	hit()

