## SELENIUM  --
## Source: AutomateTheBoringStuff.com
## bit.ly/automatetalk
## pip install selenium
## pip install pyautogui
## Common Special Key Values:
## Attributes - Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT
## Keys.Enter, Keys.Return
###  browser.back()  # browser.forward() # browser.refresh()
## Read in data from Webpage:# elem.text  # elem.get_attribute('href')
##Get ALL attributes: elem.get_attribute('outerHTML')
## '<a href="" class="main-navigation-toggle"><i class="fa fa-bars"></i></a>'

import pyautogui
# image recognition -> sudo apt-get scrot  # pixel(x, y) returns RGB tuple
# screenshot([filename]) # returns PIL/Pillow Image object [and saves to file]
#locateOnScreen(imageFilename) # returns(left, top, width, height) tuple or None
pyautogui.locateOnScreen('7key.png')

from selenium import webdriver
browser = webdriver.Firefox()
#browser.get('http://thomasmaestas.net')
browser.get('https://automatetheboringstuff.com')
elem = browser.find_element_by_css_selector('.entry-content > ol:nth-child(15) > li:nth-child(1) > a:nth-child(1)')
elem.text
elem.click()
browser.quit()
