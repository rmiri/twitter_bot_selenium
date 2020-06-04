from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

# I created another file where I stored my login and password
import password

URL = 'https://twitter.com/login'

# change this path to where the chromedriver is on your machine
CHROMEDRIVERPATH = '/Users/rmiriuk/chromedriver'

# change this to your username and password
userUsername = password.USERNAME
userPassword = password.PASSWORD

def main():
    # open the browser
    browser = webdriver.Chrome(CHROMEDRIVERPATH)
    browser.get(URL)

    # wait for the browser to be loaded
    browser.implicitly_wait(5)
    
    userInput = browser.find_element_by_name('session[username_or_email]')
    passwordInput = browser.find_element_by_name('session[password]')

    # fill with the details
    userInput.send_keys(userUsername)
    passwordInput.send_keys(userPassword)
    passwordInput.send_keys(Keys.ENTER)

    browser.implicitly_wait(5)

    tweet = browser.find_element_by_css_selector("br[data-text='true']")
    tweet.send_keys('hello')
    button = browser.find_element_by_css_selector("div[data-testid='tweetButtonInline']")
    button.click()

    time.sleep(2)
    browser.close() 
    print('finished')

main()