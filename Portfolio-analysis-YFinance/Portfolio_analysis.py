# Portfolio analysis tools via Yahoo. Pass a dictionary of {"Company name":"Yahoo_Ticker"} for a given portfolio into the companies variable,
# where only the "Yahoo_Ticker" is relevant. Select the frequency of data {"Frequency":"freq"} where only the "freq" is relevant.
# Enter the risk free rate when prompted.
# The tool calculates a correlation matrix, log returns, volatility, and Sharpe ratio for each stock in the portfolio.
# The dataframe outputs are:
#  -"df" dataframe with the closing prices of each stock in the portfolio.
#  -"sharpesdf" dataframe with the Sharpe ratio and volatility of each stock in the portfolio.
#  -"returnsdf" dataframe with the log returns of each stock in the portfolio.
#  -"corrmx" the correlation matrix of the portfolio.


import os
import requests
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd


# dictionary of company names and their stock symbols
companies = {
    "Moody's Corporation": "MCO",
    "Logitech International": "LOGI",
    "Pinterest": "PINS",
}

periods = {
    "1 day": "1d",
    "Weekly": "1wk",
    "Monthly": "1mo",
}
p = periods["1 day"]

# today's date "%Y-%m-%d"
d = datetime.datetime.now().strftime("%Y-%m-%d")
date = datetime.datetime.strptime(d, "%Y-%m-%d")
date = int(date.timestamp())

driver = webdriver.Chrome()
url = "https://finance.yahoo.com/"
driver.get(url)

try:
    driver.find_element(By.ID, "scroll-down-btn").click()
except:
    pass
finally:
    driver.find_element(By.CSS_SELECTOR,"button[name='reject']").click()

df = pd.DataFrame()

# iterate through companies and get a "data" dataframe which is then joined to the "df" dataframe
for i in companies.values():
    url = f"https://finance.yahoo.com/quote/{i}/history/?frequency={p}&period1=1571042725&period2={date}"
    driver.get(url)

    table_data = driver.find_element(By.CSS_SELECTOR, "div[class='table-container yf-j5d1ld']")
    rows = table_data.find_elements(By.CSS_SELECTOR, "tr[class='yf-j5d1ld']")

    company = {}

    for row in rows:
        values = row.find_elements(By.CSS_SELECTOR, "td[class='yf-j5d1ld']")
        values = [value.text for value in values if value == values[0] or value == values[4]]
        try:
            company[values[0]] = values[1]
        except:
            continue

    data = pd.DataFrame(company.items())
    data.columns = ["Date " + i, "Close " + i]
    data["Date " + i] = pd.to_datetime(data["Date " + i])
    data.set_index("Date " + i, inplace=True)
    data = data.dropna()
    df = df.join(data, how="outer")

# Additional formatting for UK GBPp stocks containing commas
for column in df.columns:
    df[column] = df[column].str.replace(",", "")
    df[column] = df[column].astype(float)

df = df.sort_index(ascending=False)

driver.close()

returnsdf = pd.DataFrame()

for column in df.columns:
    returns = np.log(df[column]/df[column].shift(1))
    returnsdf = returnsdf.join(returns, how="outer")

# count the number of years in returnsdf
years = len(returnsdf.index.year.unique())

# return the current year
current_year = datetime.datetime.now().year

sharpesdf = pd.DataFrame()
sharpesdf["Year"] = returnsdf.index.year.unique()
sharpesdf = sharpesdf.sort_values("Year", ascending=False)

# ask for the risk free rate
rfr = float(input("Risk Free Rate: "))

# iterate through rows in returnsdf
for i in range(0, years):
    for column in returnsdf.columns:
        volatility = returnsdf.loc[returnsdf.index.year == current_year - i, column].std() * np.sqrt(252)
        sharpesdf.loc[sharpesdf["Year"] == current_year - i, f"Volatility {column}"] = volatility
        sharpe_ratio = ((returnsdf.loc[returnsdf.index.year == current_year - i, column].mean() * 252) - rfr) / volatility
        sharpesdf.loc[sharpesdf["Year"] == current_year - i, f"Sharpe Ratio {column}"] = sharpe_ratio
        print(f"{column} {current_year - i} Sharpe Ratio: {sharpe_ratio}, Volatility: {volatility}")

# Create a correlation matrix
corrmx = returnsdf.corr()
