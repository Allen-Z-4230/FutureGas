import pandas as pd
import datetime

df_dji = pd.read_csv("DJI.csv") ## Reading DJI
df_cpi = pd.read_csv("CPI.csv") ## Reading CPI
file = pd.ExcelFile("GAS.xls")   ## Load the gas prices database

#Column selection
df_gas= file.parse('Data 1', header=2, ncolumns=2) # Parse the file, saving as our database
df_gas.drop(['U.S. All Grades Conventional Retail Gasoline Prices (Dollars per Gallon)',
           'U.S. All Grades Reformulated Retail Gasoline Prices (Dollars per Gallon)',
           'U.S. Regular All Formulations Retail Gasoline Prices (Dollars per Gallon)',
           'U.S. Regular Conventional Retail Gasoline Prices (Dollars per Gallon)',
           'U.S. Regular Reformulated Retail Gasoline Prices (Dollars per Gallon)',
           'U.S. Midgrade All Formulations Retail Gasoline Prices (Dollars per Gallon)',
           'U.S. Midgrade Conventional Retail Gasoline Prices (Dollars per Gallon)',
           'U.S. Midgrade Reformulated Retail Gasoline Prices (Dollars per Gallon)',
           'U.S. Premium All Formulations Retail Gasoline Prices (Dollars per Gallon)',
           'U.S. Premium Conventional Retail Gasoline Prices (Dollars per Gallon)',
           'U.S. Premium Reformulated Retail Gasoline Prices (Dollars per Gallon)',
           'U.S. No 2 Diesel Retail Prices (Dollars per Gallon)',
           'U.S. No 2 Diesel Ultra Low Sulfur (0-15 ppm) Retail Prices (Dollars per Gallon)',
           'U.S. No 2 Diesel Low Sulfur (15-500 ppm) Retail Prices (Dollars per Gallon)'],
           axis = 1, inplace = True)
df_gas['Date'] = df_gas.Date + pd.offsets.MonthBegin(1) #setting date from the 15th to the 1st
df_dji = df_dji[['Date', 'Close']]

#Dropping NaN values
df_gas.dropna(axis=0, inplace=True)
df_cpi.dropna(axis=0, inplace=True)
df_dji.dropna(axis=0)

#Converting dates from string to datetime
df_dji['Date'] = pd.to_datetime(df_dji.Date)
df_cpi['Date'] = pd.to_datetime(df_dji.Date)

#merging
df = df_dji.merge(df_cpi, how='inner', on='Date')
df = df.merge(df_gas, how='inner', on='Date')

print(len(df))
