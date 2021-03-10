import re

import pandas as pd
import collections

import requests
import wget
import urllib.request
from bs4 import BeautifulSoup


def read_csv(path):
    df = pd.read_csv(path, skiprows=9, usecols=['ISIN', 'Name', 'Weight (%)', 'Location'])
    df["Weight (%)"] = pd.to_numeric(df["Weight (%)"])
    df = df.loc[df["Weight (%)"] > 0]

    df = df[['ISIN', 'Name', 'Weight (%)', 'Location']]
    df.columns = ['ISIN', 'name', 'weight', 'location']
    df.attrs['path'] = path
    # TODO add name of etf

    return df


def get_file(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    suburl = soup.select('#holdings > div.holdings.fund-component-data-export > a.icon-xls-export')[0].get('href')

    # set filename
    search = 'fileName=[a-zA-Z]*'
    x = re.findall(search, suburl)
    filename = x[0].split("=")[1] + ".csv"

    # Download file
    #filepath = wget.download(url + suburl, out=filename)
    with urllib.request.urlopen(url + suburl) as f:
        html = f.read().decode('utf-8')
        with open(filename, 'w', encoding="utf-8") as out:
            out.write(html)

    return filename

def getFromURL(url):
    file = get_file(url)
    df = read_csv(file)
    return df







if __name__ == '__main__':
    d = read_csv('ICLN_holdings.csv')
    print(d.head())
    print(d.shape)

    d = getFromURL('https://www.ishares.com/us/products/239738/')
    print(d.head())
    print(d.shape)