# if someone queries for sth the porgram should fetch the info from wikipedia
# we use selenium web driver for this functionalty

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# import pyttsx3 as p
# # from webdriver_manager.chrome import ChromeDriverManager
# # from selenium.webdriver.common.by import By

# engine = p.init()

# # initialize a p instance in class. init
# engine = p.init()

# # get voice properties
# rate = engine.getProperty('rate')

# # change rate of the sound
# engine.setProperty('rate', 130)

# # see what voices the library provides for us
# voices= engine.getProperty('voices')
# # print(voices)

# engine.setProperty('voice', voices[1].id)


class infow():
    def __init__(self):
        s = Service('C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe')
        self.driver= webdriver.Chrome(service=s)

    def get_info(self, query):
        self.query= query
        self.driver.get(url="http://www.wikipedia.org")
        search = self.driver.find_element('xpath','//*[@id="searchInput"]')
        # driver goes to the line of code
        search.click()
        # query to be inputted in searchbox
        search.send_keys(query)
        enter = self.driver.find_element('xpath',
            '//*[@id="search-form"]/fieldset/button')
        enter.click()
        # read= self.driver.find_element('xpath','//*[@id="mw-content-text"]/div[1]/p[1]')
        # read.click()
        # engine.say(read)
        # engine.runAndWait()

