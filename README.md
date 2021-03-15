# Calculate ETF Overlap

This tool can be used to check if the money is well distributed (invested broadly and diversified) when investing in multiple ETF's.

Currently only iShares links are supported.


### Example

In the following Example we can see that the two etfs overlap significantly. There are 466 positions contained in both etfs and over 80% of the money is invested in the US which may not have been your goal.
```text
> python main.py https://www.ishares.com/us/products/239726/ https://www.ishares.com/us/products/239696/

+--------------------------+-------------------------------------+-------------------------------------+---------------------------+
|                          |                Total                |       iShares Core S&P 500 ETF      |   iShares MSCI World ETF  |
+--------------------------+-------------------------------------+-------------------------------------+---------------------------+
|        Positions         |                 1285                |                 508                 |            1257           |
+--------------------------+-------------------------------------+-------------------------------------+---------------------------+
|  Overlapping Positions   |                 466                 |                                     |                           |
| (contained in every ETF) |                                     |                                     |                           |
+--------------------------+-------------------------------------+-------------------------------------+---------------------------+
|         Top Ten          | 4.8% APPLE INC                      | 5.8% APPLE INC                      | 3.8% APPLE INC            |
|                          | 4.2% MICROSOFT CORP                 | 5.3% MICROSOFT CORP                 | 3.1% MICROSOFT CORP       |
|                          | 3.2% AMAZON COM INC                 | 3.9% AMAZON COM INC                 | 2.4% AMAZON COM INC       |
|                          | 1.6% FACEBOOK CLASS A INC           | 1.9% FACEBOOK CLASS A INC           | 1.2% FACEBOOK CLASS A INC |
|                          | 1.5% ALPHABET INC CLASS A           | 1.8% ALPHABET INC CLASS A           | 1.1% ALPHABET INC CLASS C |
|                          | 1.5% ALPHABET INC CLASS C           | 1.8% ALPHABET INC CLASS C           | 1.1% ALPHABET INC CLASS A |
|                          | 1.3% TESLA INC                      | 1.6% TESLA INC                      | 1.0% TESLA INC            |
|                          | 1.1% JPMORGAN CHASE & CO            | 1.5% BERKSHIRE HATHAWAY INC CLASS B | 0.9% JPMORGAN CHASE & CO  |
|                          | 1.1% BERKSHIRE HATHAWAY INC CLASS B | 1.4% JPMORGAN CHASE & CO            | 0.8% JOHNSON & JOHNSON    |
|                          | 1.0% JOHNSON & JOHNSON              | 1.3% JOHNSON & JOHNSON              | 0.7% VISA INC CLASS A     |
|                          |                                     |                                     |                           |
+--------------------------+-------------------------------------+-------------------------------------+---------------------------+
|       Sum Top Ten        |                21.2 %               |                26.4 %               |           16.1 %          |
+--------------------------+-------------------------------------+-------------------------------------+---------------------------+
|      Top Locations       |         83.2% United States         |         100.0% United States        |    66.2% United States    |
|                          |         3.8%  Japan                 |                                     |    7.6%  Japan            |
|                          |         2.2%  United Kingdom        |                                     |    4.4%  United Kingdom   |
|                          |         1.7%  France                |                                     |    3.4%  France           |
|                          |         1.6%  Canada                |                                     |    3.3%  Canada           |
|                          |         1.4%  Germany               |                                     |    2.9%  Germany          |
|                          |         1.4%  Switzerland           |                                     |    2.8%  Switzerland      |
|                          |         1.1%  Australia             |                                     |    2.2%  Australia        |
|                          |         0.6%  Netherlands           |                                     |    1.2%  Netherlands      |
|                          |         0.6%  Sweden                |                                     |    1.1%  Sweden           |
|                          |         0.5%  Hong Kong             |                                     |    1.0%  Hong Kong        |
|                          |         0.4%  Italy                 |                                     |    0.8%  Italy            |
|                          |         0.4%  Spain                 |                                     |    0.7%  Spain            |
|                          |         0.4%  Denmark               |                                     |    0.7%  Denmark          |
|                          |         0.2%  Finland               |                                     |    0.3%  Singapore        |
|                          |         0.2%  Singapore             |                                     |    0.3%  Finland          |
|                          |         0.2%  Belgium               |                                     |    0.3%  Belgium          |
|                          |         0.1%  Ireland               |                                     |    0.2%  Ireland          |
|                          |         0.1%  Norway                |                                     |    0.2%  Norway           |
|                          |         0.1%  Israel                |                                     |    0.2%  Israel           |
|                          |         0.0%  Portugal              |                                     |    0.1%  New Zealand      |
|                          |         0.0%  New Zealand           |                                     |    0.1%  Portugal         |
|                          |         0.0%  Austria               |                                     |    0.1%  Austria          |
|                          |                                     |                                     |    0.0%  European Union   |
|                          |                                     |                                     |                           |
+--------------------------+-------------------------------------+-------------------------------------+---------------------------+
```

### Installation
Option 1: Download pre-build binaries here: [https://github.com/sorgmi/pyetfoverlap/releases/latest](https://github.com/sorgmi/pyetfoverlap/releases/latest)

Option 2: Pip
```text
git clone https://github.com/sorgmi/pyetfoverlap
pip install -r requirements.txt
python main.py https://www.ishares.com/us/products/239726/ [...]
```