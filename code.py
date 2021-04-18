from selenium import webdriver
import time
import os
import subprocess
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.headless = True
path = os.getcwd()+"/geckodriver"
def hit():
	try:
		driver = webdriver.Firefox(options=opts,executable_path=path)
		print(driver)
		driver.get("http://www.slutbags.tk")
		print(driver)
		print(driver.window_handles)
		body = driver.find_elements_by_class_name("text-center")
		print(body)
		body[0].click()
		print(driver.window_handles)
		print("Switching from " + driver.title + " to ")
		driver.switch_to.window(driver.window_handles[1])
		print(driver.title)
		ads = driver.find_elements_by_tag_name("iframe")
		print(ads)
		ads[0].click()
		print("All tab after process")
		print(driver.window_handles)
		time.sleep(2)
		for tab in driver.window_handles:
			driver.switch_to.window(tab)
			print("Closing " + driver.title)
			driver.close()
		subprocess.run(['sudo','./delete-profiles.sh'])
	except Exception:
		subprocess.run(['sudo','python3','code.py'])
while True:
	hit()

