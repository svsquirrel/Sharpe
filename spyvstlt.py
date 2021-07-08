import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 9)

timeperiod = 90

#Sharpe ratio = Return - Risk Free Rate / Std Deviation

df = pd.read_csv('VTI.csv') 
df =df[ ['Date' ,'Adj Close']]
df = df.rename (columns={'Adj Close': 'VTI'})
df['Date']= pd.to_datetime(df['Date'])

dfb = pd.read_csv('BND.csv') 
dfb =dfb[ ['Date' ,'Adj Close']]
dfb = dfb.rename (columns={'Adj Close': 'BND'})
dfb['Date']= pd.to_datetime(dfb['Date'])

df = df.merge( dfb, on="Date", how='left')

#Get the % daily returns for the ETF's 
df['VTIret'] = 100*(df['VTI']/df['VTI'].shift(timeperiod) - 1)
df['BNDret'] = 100*(df['BND']/df['BND'].shift(timeperiod) - 1)

#Get rolling standard deviation for the ETF
df['VTIstd'] = df['VTIret'].rolling(timeperiod).std()
df['BNDstd'] = df['BNDret'].rolling(timeperiod).std()

#Now calculate the sharpe ratio
df['VTIsharpe'] = df['VTIret'] / df['VTIstd']
df['BNDsharpe'] = df['BNDret'] / df['BNDstd']
print(df.tail(90))
#Plot the data
# you can plat the two separately by using the first 2 statments, or related to each other
#by using the 3rd statement
plt.plot(df['Date'],df['BNDsharpe'], label = 'BND')
plt.plot(df['Date'], df['VTIsharpe'],label='VTI')
#plt.plot(df['Date'], df['VTIsharpe'] - df['BNDsharpe'], label="VTI - BND")
plt.title("Sharpe ratios")
plt.legend()

#plt.show()
