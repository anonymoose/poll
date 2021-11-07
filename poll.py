from selenium import webdriver
import time
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options


class Bot:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=1900,1080")
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver",
                                       options=options)

    def vote(self):
        # open up the page
        print("open site")

        self.driver.get('https://www.app.com/story/sports/high-school/field-hockey/2021/11/06/vote-shore-conference-field-hockey-star-njsiaa-week-2/6301409001/')

        time.sleep(5)

        # clear the add at the top
        try:
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            # hover_button = self.driver.find_element_by_xpath("/html/body/div[7]/div/button")
            # hover_button.click()
            # hit escape for good measure
        except Exception as ex:
            print(ex)
            pass

        # scroll the wrapper div into view.  sometimes its in different places.
        self.scroll("/html/body/div[1]")
        self.scroll("/html/body/div[2]")
        # self.scroll("/html/body/div[2]/main/article/div[1]")
        # self.scroll("/html/body/div[2]/main/article/div[2]")
        # self.scroll("/html/body/div[2]/main/article/div[3]")
        # self.scroll("/html/body/div[2]/main/article/div[4]")
        # self.scroll("/html/body/div[2]/main/article/div[4]/aside[1]")
        # self.scroll("/html/body/div[2]/main/article/div[4]/aside[2]")

        print("start clicking buttons")

        # find the iframe we're in and switch to it.
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe.gnt_em_hf_if")))

        # find the checkbox for our girl
        chkbox = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#PDI_answer50402302")))
        chkbox.click()
        time.sleep(0.5)

        # wait for the vote button to be clickable and click it
        vote = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a#pd-vote-button10959518")))
        self.driver.save_screenshot("screenshot.png")
        vote.click()

        # be nice.
        time.sleep(3.0)

        # close the browser.
        print("closing.")
        self.driver.quit()


    def scroll(self, xpath):
        # scroll something into view
        # https://stackoverflow.com/questions/3401343/scroll-element-into-view-with-selenium
        try:
            poll_wrapper = self.driver.find_element_by_xpath("/html/body/div[2]/main/article/div[4]/aside[2]")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", poll_wrapper);
            time.sleep(1.0)
        except:
            pass


if __name__ == '__main__':


    while True:
        b = Bot()
        b.vote()
        time.sleep(3)
