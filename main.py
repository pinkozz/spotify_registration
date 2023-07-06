# Read README.md for proper instructions on how to use this program
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains, Keys
import time

browser = webdriver.Firefox()
browser.get('https://www.spotify.com/ua-en/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F')
def mail():
    # Set email
    setEmail = browser.find_element('id', 'email')
    setEmail.send_keys('mail@example.com')

def password():
    # Set password
    setPassword = browser.find_element('id', 'password')
    setPassword.send_keys('PASSWORD')

def name():
    # Set name
    setName = browser.find_element('id', 'displayname')
    setName.send_keys('name')
    
def birthday():
    # Set day
    setDay = browser.find_element('id', 'day')
    setDay.send_keys('1')
    # Set month
    setMonth = browser.find_element('id', 'month')
    setMonth.send_keys('December')
    # Set year
    setYear = browser.find_element('id', 'year')
    setYear.send_keys('2000')

def gender():
    # Set gender
    actions = ActionChains(browser)
    setGender = browser.find_element('css selector', '#gender_option_prefernottosay')
    setGender.send_keys(Keys.END)
    time.sleep(2)  # If you launch this program on fast computer with fast internet you can remove this line of code, but it`s not recommended to remove it
    actions.click(setGender).perform()

def terms():
    # Accept Spotify terms of usage
    actions = ActionChains(browser)
    acceptTerms = browser.find_element('css selector', '#terms-conditions-checkbox')
    actions.click(acceptTerms).perform()
    acceptTerms.submit()

def main():
    mail()
    password()
    name()
    birthday()
    gender()
    terms()

if __name__ == '__main__':
    main()
