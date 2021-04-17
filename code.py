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
	print("Opening browser...")
	driver = webdriver.Firefox(options=opts,executable_path=path)
	print(driver)
	print("Browser opened...")
	time.sleep(3)

	# Load Page
	print("Loading page...")
	driver.get("http://www.slutbags.tk")
	print(driver)
	print("Page loaded...")
	time.sleep(3)

	print(driver.window_handles)
	# Scroll home page
	print("Scrolling page... " + driver.title)
	driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	time.sleep(3)

	# Scroll back up
	driver.execute_script("window.scrollTo(0,0)")
	print("Done Scrolling page..." + driver.title)

	# Find popunder element
	print("Getting body of page: " + driver.title)
	body = driver.find_elements_by_class_name("text-center")
	print(body)

	# Click Popunder element
	print("Clicking Popunder element of " + driver.title)
	body[0].click()
	time.sleep(3)
	print(driver.window_handles)

	# Switch window to popunder ad
	print("Switching pages from " + driver.title + " to ")
	driver.switch_to.window(driver.window_handles[0])
	print(driver.title)
	time.sleep(5)

	# Scroll Popunder ad
	print("Scrolling page: " + driver.title)
	driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	time.sleep(3)

	# Switch window back to home page
	print("Switching from " + driver.title + " to ")
	driver.switch_to.window(driver.window_handles[1])
	print(driver.title)
	time.sleep(3)

	# Get Ad element
	print("Getting ad element on " + driver.title)
	ads = driver.find_elements_by_tag_name("iframe")
	print(ads)

	# Click ad elemement
	print("Clicking ad elements on " + driver.title)
	ads[0].click()
	time.sleep(3)
	print(driver.window_handles)

	# Switch window to text ad
	print("Switching from " + driver.title + " to -----> ERR HERE | DEH IS NOT AD RENDERING ")
	if len(driver.window_handles)) == 3:
		driver.switch_to.window(driver.window_handles[2])
		print(driver.title)
		time.sleep(5)

		# Scroll the ad page
		print("Scrolling page: " + driver.title )
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		time.sleep(3)

	# Switch page to home
	print("Switching from page " + driver.title + " to home page... ")
	driver.switch_to.window(driver.window_handles[1])
	print(driver.title)
	time.sleep(3)


	# Closing tabs
	print("Closing tabs...")
	print(driver.window_handles)
	for tab in driver.window_handles:
		driver.switch_to.window(tab)
		print("Closing " + driver.title)
		time.sleep(3)
		driver.close()

	subprocess.run(['sudo','./delete-profiles.sh'])

while True:
	hit()

