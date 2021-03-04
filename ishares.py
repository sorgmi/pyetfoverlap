import pandas as pd
import collections


def read_csv(path):
    df = pd.read_csv(path, skiprows=9, usecols=['ISIN', 'Name', 'Weight (%)', 'Location'])
    df["Weight (%)"] = pd.to_numeric(df["Weight (%)"])
    df = df.loc[df["Weight (%)"] > 0]

    df = df[['ISIN', 'Name', 'Weight (%)', 'Location']]
    df.columns = ['ISIN', 'name', 'weight', 'location']
    df.attrs['path'] = path
    # todo add name of etf

    return df












if __name__ == '__main__':
    d = read_csv('ICLN_holdings.csv')
    print(d.head())
    print(d.shape)