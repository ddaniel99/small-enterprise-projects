<b> DESCRIPTION </b> <br>
 This is a portfolio analysis tool taking a dictionary of Yahoo tickers and returning log price changes, a correlation matrix, annual volatilities and annual Sharpe ratios. 


<br><br>
<b> Portfolio_analysis.py </b><br>
 Portfolio analysis tools via Yahoo. Pass a dictionary of {"Company name":"Yahoo_Ticker"} for a given portfolio into the companies variable, where only the "Yahoo_Ticker" is relevant. Select the frequency of data {"Frequency":"freq"} where only the "freq" is relevant.
<br>
Enter the risk free rate when prompted.
<br>
The tool calculates a correlation matrix, log returns, volatility, and Sharpe ratio for each stock in the portfolio per years in the portfolio.
<br>
The dataframe outputs are:
  -<b>"df"</b> dataframe with the closing prices of each stock in the portfolio.
  -<b>"sharpesdf"</b> dataframe with the Sharpe ratio and volatility of each stock in the portfolio.
  -<b>"returnsdf"</b> dataframe with the log returns of each stock in the portfolio.
  -<b>"corrmx"</b> the correlation matrix of the portfolio.