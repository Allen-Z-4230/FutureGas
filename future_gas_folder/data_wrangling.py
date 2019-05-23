import pandas as pd
import datetime

df_dji = pd.read_csv("data/DJI.csv") ## Reading DJI
df_sp500 = pd.read_csv('data/S&P500.csv')
df_nas = pd.read_csv('data/NASDAQ.csv')
file = pd.ExcelFile("data/GAS.xls")   ## Load the gas prices database

#Column selection
df_gas= file.parse('Data 1', header=2, ncolumns=2) # Parse the file, saving as our database
df_gas = df_gas[['Date', 'Weekly U.S. All Grades All Formulations Retail Gasoline Prices  (Dollars per Gallon)']]
df_gas = df_gas.rename(index=str,
    columns={"Weekly U.S. All Grades All Formulations Retail Gasoline Prices  (Dollars per Gallon)": "gas_price"})
df_dji = df_dji[['Date', 'Close', 'Adj Close']]
df_sp500 = df_sp500[['Date', 'Close', 'Adj Close']]
df_nas = df_nas[['Date', 'Close', 'Adj Close']]

#Dropping NaN values
df_gas.dropna(axis=0, inplace=True)
df_sp500.dropna(axis=0, inplace=True)
df_dji.dropna(axis=0, inplace=True)
df_nas.dropna(axis=0, inplace=True)

#Converting dates from string to datetime
df_gas['Date'] = pd.to_datetime(df_gas.Date)
df_dji['Date'] = pd.to_datetime(df_dji.Date)
df_sp500['Date'] = pd.to_datetime(df_sp500.Date)
df_nas['Date'] = pd.to_datetime(df_nas.Date)

print(len(df_gas),len(df_dji), len(df_sp500), len(df_nas))
