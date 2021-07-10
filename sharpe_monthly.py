import pandas as pd
import numpy as np
import pandas_datareader as web
pd.set_option('display.max_rows', 15)

riskfreerate = 0.05
filename_one = 'VTImonthly.csv'
#if monthly annualization enter 12, if daily use 252
annualize = 12


df = pd.read_csv(filename_one) 
df =df[ ['Adj Close']]
df = df.rename (columns={'Adj Close': 'A'})

#get percent change rate of returns
etf_pct = df['A'].pct_change()

mean = etf_pct.mean()

#calculate the standard deviation and annualize it
std = etf_pct.std()
std  = std*np.sqrt(annualize)

#get the rate of returns for the etf
etf_return = (df.iloc[-1] / df.iloc[0]) -1


sharpe = (etf_return - riskfreerate) / std

print(sharpe)

