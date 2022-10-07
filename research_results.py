from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

S = Service(os.environ["DRIVER_LOCATION"])
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSe1OJgtUlA3lulx1Gays4hkbl9GfE2GxarcFDCR6Fd5xaKIsw/" \
           "viewform?usp=sf_link"


class ResearchResults:
    def __init__(self):
        self.driver = webdriver.Chrome(service=S)

    def fill_in_form(self, address, price, property_link):
        self.driver.get(FORM_URL)
        time.sleep(2)
        self.driver.find_element(
            By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input"
        ).send_keys(address)
        self.driver.find_element(
            By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"
        ).send_keys(price)
        self.driver.find_element(
            By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input"
        ).send_keys(property_link)
        self.driver.find_element(
            By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div"
        ).click()

    def quit(self):
        self.driver.quit()
