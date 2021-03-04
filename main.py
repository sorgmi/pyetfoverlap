import collections

import pandas as pd
from prettytable import PrettyTable

import ishares

def merge(dataframes):
    merged = {}
    for df in dataframes:
        for index, row in df.iterrows():
            if row["ISIN"] not in merged.keys():
                merged[row["ISIN"]] = {}
                positiondict = merged[row["ISIN"]]
                positiondict["name"] = row["name"]
                positiondict["weight"] = row["weight"]
                positiondict["location"] = row["location"]
            else:
                positiondict = merged[row["ISIN"]]
                positiondict["weight"] += row["weight"]

    for key in merged.keys():
        merged[key]["weight"] /= len(dataframes)

    #merged = collections.OrderedDict(sorted(merged.items(), key=lambda x: x[1]["weight"], reverse=True))

    data = []
    for k,v in merged.items():
        data.append((k,v["name"],v["weight"],v["location"]))

    df = pd.DataFrame(data=data, columns=['ISIN', 'name', 'weight', 'location'])
    return df


def format_table_string(alist, delimiter=" - "):
    col_width = [max(len(x) for x in col) for col in zip(*alist)]
    s = ""
    for line in alist:
        s += "" + delimiter.join("{:{}}".format(x, col_width[i])for i, x in enumerate(line)) + ""
        s += "\n"
    return s


def printTable(merged, dataframes):
    all_dataframes = [merged, *dataframes]
    table = PrettyTable()
    table.field_names = ["", "Total"] + [df.attrs['path'] for df in dataframes]
    table.hrules = True

    # Total Positions
    row = ['Positions'] + [df.shape[0] for df in all_dataframes]
    table.add_row(row)

    # Top Ten Positions
    row = ['Top Ten']
    for df in all_dataframes:
        top = df.nlargest(10, 'weight')
        top = top[["name", "weight"]]
        total = sum(top["weight"].values)
        textstr = format_table_string([(str(round(b, 1))+"%", str(a)) for a,b in top.values], delimiter=" ")
        row.append(textstr)
    table.add_row(row)

    # Sum of Top Ten Positions
    row = ['Sum Top Ten']
    for df in all_dataframes:
        top = df.nlargest(10, 'weight')
        top = top[["name", "weight"]]
        total = sum(top["weight"].values)
        textstr = f"{total} %"
        row.append(textstr)
    table.add_row(row)

    # Locations
    row = ['Top Locations']
    for df in all_dataframes:
        d = collections.defaultdict(int)
        for l, w in df[['location', 'weight']].values:
            d[l] += w

        d = collections.OrderedDict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        textstr = format_table_string([(str(round(b, 1))+"%", str(a)) for a,b in d.items()], delimiter=" ")
        row.append(textstr)
    table.add_row(row)

    print(table)


if __name__ == '__main__':
    d1 = ishares.read_csv('ICLN_holdings.csv')
    d2 = ishares.read_csv('IVV_holdings.csv')
    merged = merge([d1, d2])
    printTable(merged, [d1, d2])

