import pandas as pd
import os
import time as t
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Selenium Configuration
path = os.path.abspath(os.path.join(os.path.normpath(os.path.dirname(__file__)), 'chromedriver.exe'))
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('log-level=3')
chrome_options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(executable_path=path, options=chrome_options)

def crawler_skiresort_ch():
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

    df.to_csv('../Data/Output_Skiresort_ch.csv', index=False)

    # Close the webdriver
    driver.close()

crawler_skiresort_ch()