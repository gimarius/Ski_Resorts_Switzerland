import pandas as pd
import re
from datetime import date
from datetime import timedelta
from datetime import datetime
import numpy as np
import openpyxl


def crawler_my_switerland_daily():
    # Get the data from the Website
    url = 'https://www.bergfex.ch/schweiz/schneewerte/'
    dfs = pd.read_html(url)
    df = dfs[0]

    # Split column Lifte in Offene Bahnen and Total Bahnen
    df[['Offene_Bahnen', 'Total_Bahnen']] = df['Lifte'].str.split("/", expand=True)

    # Create variables for the dates
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    today = today.strftime('%d.%m.%Y')
    yesterday = yesterday.strftime('%d.%m.%Y')

    # Strings are replaces by datetime values
    df['Date'] = df['Datum'].str.replace('Heute', today)
    df['Date'] = df['Date'].str.replace('Gestern', yesterday)

    # Drop useless column
    df.drop(columns=df.columns[4], axis=1, inplace=True)

    # Split Date and Time
    df[['Date', 'Time']] = df['Date'].str.split(",", expand=True)

    # Drop seless column
    df.drop(columns=df.columns[4], axis=1, inplace=True)

    # Replace strings with na-values
    df['Date'] = df['Date'].str.replace('Mo', '')
    df['Date'] = df['Date'].str.replace('Di', '')
    df['Date'] = df['Date'].str.replace('Mi', '')
    df['Date'] = df['Date'].str.replace('Do', '')
    df['Date'] = df['Date'].str.replace('Fr', '')
    df['Date'] = df['Date'].str.replace('Sa', '')
    df['Date'] = df['Date'].str.replace('So', '')

    # Replace values with values from another column
    df['Date'] = np.where(df['Date'] == '', df['Time'], df['Date'])

    # Drop useless column
    df.drop(columns=df.columns[7], axis=1, inplace=True)

    # Drop useless strings
    df['Tal'] = df['Tal'].map(lambda x: x.lstrip('+-').rstrip('cm'))
    df['Berg'] = df['Berg'].map(lambda x: x.lstrip('+-').rstrip('cm'))
    df['Neu'] = df['Neu'].map(lambda x: x.lstrip('+-').rstrip('cm'))

    # Rename column names
    df = df.rename(
        columns={'Tal': 'Schnee_Tal_in_cm', 'Berg': 'Schnee_Berg_in_cm', 'Neu': 'Neuschnee_in_cm', 'Date': 'Datum'})

    # Save to Excel File
    today = datetime.today()
    today_str = today.strftime('%d-%m-%Y')
    df.to_excel('../Data/'+ today_str + '_Output_MySwitzerland_daily.xlsx', index=False)
    return df


crawler_my_switerland_daily()
