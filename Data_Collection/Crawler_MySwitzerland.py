import pandas as pd
import os
import time as t
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Selenium Config
path = os.path.abspath(os.path.join(os.path.normpath(os.path.dirname(__file__)), '../chromedriver.exe'))
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


