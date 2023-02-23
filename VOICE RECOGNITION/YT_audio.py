from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

class music():
    def __init__(self):
        s = Service('C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe')
        self.driver= webdriver.Chrome(service=s)

    def play(self, query):
        self.query= query
        self.driver.get(url="http://www.youtube.com/results?search_query=" + query)
        video= self.driver.find_element('xpath','//*[@id="dismissible"]')
        video.click()

