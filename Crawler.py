import pandas as pd
import os
import time as t
import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


# Selenium Config
path = os.path.abspath(os.path.join(os.path.normpath(os.path.dirname(__file__)), 'chromedriver.exe'))
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('log-level=3')
chrome_options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(executable_path=path, options=chrome_options)


def skiresort_crawler_myswitzerland():
    driver.get('https://snow.myswitzerland.com/schneebericht/')
    t.sleep(2)
    i = 0

    df = pd.DataFrame([])

    while i < 9:
        i = i + 1

        # Find all the xpath elements on the page
        xpath_element = driver.find_elements('xpath',
                                         '/html/body/div/div[1]/form/div[2]/div/div[1]/div/div[1]/div[2]/div[2]/table/tbody/tr')
        # Extract the text from each xpath element
        texts = [element.text for element in xpath_element]
        texts = pd.Series(texts)
        print(texts)

        # Append texts to array
        df = pd.concat([df, texts])

        #Move to another site
        url = 'https://snow.myswitzerland.com/schneebericht/?p=' + str(i)
        driver.get(url)
        t.sleep(1)

    print(df)
    df.to_csv('Output_Skiresort_MySwitzerland.csv', index=False)

    # Close the webdriver
    driver.close()



def skiresort_crawler_1():
    driver.get('https://www.skiresort.ch/skigebiete/schweiz/')
    t.sleep(1)

    i = 1

    df = pd.DataFrame([])
    while i < 4:
        i = i + 1

        # Find all the xpath elements on the page
        xpath_element = driver.find_elements('xpath',
                                             '/html/body/div[2]/div[4]/div/div[1]/section/section[3]/div/div[2]/div[1]/div')

        # Extract the text from each h3 element
        text = [element.text for element in xpath_element]
        text = pd.Series(text)
        print(text)

        # Append texts to array
        df = pd.concat([df, text])

        url = 'https://www.skiresort.ch/skigebiete/schweiz/seite/' + str(i)
        driver.get(url)
        t.sleep(1)


    print(df)
    df.to_csv('Output_Skiresort_ch.csv', index=False)

    # Close the webdriver
    driver.close()











