from selenium import webdriver
import time
import os
import subprocess
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.headless = True
path = os.getcwd()+"/geckodriver"
def hit():
	driver = webdriver.Firefox(options=opts,executable_path=path)
	print(driver)
	driver.get("http://www.slutbags.tk")
	print(driver)
	ads = driver.find_elements_by_tag_name("iframe")
	print(ads)
	ads[0].click()
	print("All tab after process")
	print(driver.window_handles)
	time.sleep(3)
	for tab in driver.window_handles:
		driver.switch_to.window(tab)
		print("Closing " + driver.title)
		driver.close()
	subprocess.run(['sudo','./delete-profiles.sh'])
while True:
	hit()

