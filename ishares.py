import csv
import os
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

    # add ETF Name
    with open(path, "r", encoding="utf-8-sig", errors="ignore") as f:
        name = f.readline()
        df.attrs['etfname'] = name.strip()

    return df


def get_file(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    suburl = soup.select('#holdings > div.holdings.fund-component-data-export > a.icon-xls-export')[0].get('href')

    # set filename
    search = 'fileName=[a-zA-Z]*'
    x = re.findall(search, suburl)
    filename = x[0].split("=")[1] + ".csv"

    tmp_dir = "etf_data"
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

    file = os.path.join(tmp_dir, filename)

    # Download file
    #filepath = wget.download(url + suburl, out=filename)
    with urllib.request.urlopen(url + suburl) as f:
        html = f.read().decode('utf-8')
        with open(file, 'w', encoding="utf-8") as out:
            out.write(html)

    return file

def get_df(url):
    file = get_file(url)
    df = read_csv(file)
    return df

def getFromURL(url):
    file = get_file(url)
    df = read_csv(file)
    return df







if __name__ == '__main__':
    #d = read_csv('ICLN_holdings.csv')
    #print(d.head())
    #print(d.shape)

    d = getFromURL('https://www.ishares.com/us/products/239696/')
    print(d.head())
    print(d.shape)