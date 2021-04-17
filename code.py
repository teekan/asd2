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
	driver = webdriver.Firefox(options=opts,executable_path=path)
	time.sleep(3)

	# Load Page
	driver.get("http://www.slutbags.tk")
	time.sleep(3)

	# Scroll home page
	driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	time.sleep(3)

	# Scroll back up
	driver.execute_script("window.scrollTo(0,0)")

	# Find popunder element
	body = driver.find_elements_by_class_name("text-center")
	print(body)

	# Click Popunder element
	body[0].click()
	time.sleep(3)

	# Switch window to popunder ad
	driver.switch_to.window(driver.window_handles[0])
	time.sleep(5)

	# Scroll Popunder ad
	driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	time.sleep(3)

	# Switch window back to home page
	driver.switch_to.window(driver.window_handles[1])
	time.sleep(3)

	# Get Ad element
	ads = driver.find_elements_by_tag_name("iframe")
	print(ads)

	# Click ad elemement
	ads[0].click()
	time.sleep(3)

	# Switch window to text ad
	driver.switch_to.window(driver.window_handles[2])
	time.sleep(5)

	# Scroll the ad page
	driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	time.sleep(3)

	# Switch page to home
	driver.switch_to.window(driver.window_handles[1])
	time.sleep(3)

	for tab in driver.window_handles:
		driver.switch_to.window(tab)
		time.sleep(3)
		driver.close()

	subprocess.run(['sudo','./delete-profiles.sh'])

while True:
	hit()

