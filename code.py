from selenium import webdriver
import time
import os
import subprocess
from selenium.webdriver.firefox.options import Options
#opts = Options()
#opts.headless = True
path = os.getcwd()+"/geckodriver"
def hit():
	try:
		driver = webdriver.Firefox(executable_path=path)
		driver.get("http://www.slutbags.tk")
		ads = driver.find_elements_by_tag_name("iframe")
	except Exception:
		subprocess.run(["sudo","./kill-gecko"])

	try:
		ads[0].click()
		time.sleep(3)
		driver.switch_to.window(driver.window_handles[1])
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		time.sleep(1)
		driver.execute_script("window.scrollTo(0,0)")
		time.sleep(1)
		driver.close()
	except Exception:
		subprocess.run(["sudo","./kill-firefox"])
		subprocess.run(["sudo","./kill-gecko"])
	try:
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(1)
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		time.sleep(1)
		driver.execute_script("window.scrollTo(0,0)")
		time.sleep(1)
		driver.close()
		subprocess.run(["sudo","./delete-profiles"])
	except Exception:
		print("Didn't complete workflow")
	"""
	print("All tab after process")
	print(driver.window_handles)
	driver.switch_to.window(driver.window_handles[0])
	tabs = driver.window_handles
	rev_tabs = tabs[::-1]
	for x in range(len(driver.window_handles)):
		driver.switch_to.window(rev_tabs[x])
		print("Closing " + driver.title)
		driver.close()
	subprocess.run(['sudo','./delete-profiles'])
	"""
while True:
	hit()

