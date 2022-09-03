#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 17:49:14 2022

@author: uri
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <--- format of read_csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

#summary of the data
data.info()

#Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Mathematical Operations on Tableau
ProfitPerItem = 21.11 - 11.73
ProfitPerItem = 21.11 * 11.73
ProfitPerItem = 21.11 / 11.73
ProfitPerItem = 21.11 + 11.73

ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = ProfitPerItem * NumberOfItemsPurchased
CostPerTransaction = CostPerItem * NumberOfItemsPurchased
SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased

#Variable = dataframe ['column_name'] <--- Hacer que toda una columna sea una variable
CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#Add a new column to a dataframe
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']
data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction']

#Round markup
data['Markup'] = round(data['Markup'],2)

print(data['Day'].dtype)

#Combert number to text
Day = data['Day'].astype(str)
Year = data['Year'].astype(str)

#Combining data fields
data['Date'] = Day + '-' + data['Month'] + '-' + Year


#Using iloc to view specific columns/rows
data.iloc[0]     #View row 0
data.iloc[0:3]   #View the 3 first rows
data.iloc[-5:]   #View the last 5 rows
data.head(5)     #View the first 5 rows
data.iloc[:,2]   #View the colum 2 of all the rows
data.iloc[4,2]   #View column 2 of 4 row 



#using split to split the client_keyword field
#new_var = column.str.split ('sep',expand = True)
split_col = data['ClientKeywords'].str.split(',' , expand = True)

#adding columns
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']' , '')

#using the lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files
#bringing in a new dataset



seasons = pd.read_csv('value_inc_seasons.csv')

split_col2 = seasons['Month;Season'].str.split(';' , expand = True)
seasons['Month'] = split_col2[0]
seasons['Season'] = split_col2[1]

#dropping columns
# df = df.drop('column_name' , axis = 1)
seasons = seasons.drop(labels = 'Month;Season', axis = 1)
data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Year', 'Month'], axis = 1)


#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')
data = pd.merge(data, seasons, on = 'Month')

#export into csv
data.to_csv('ValueInc_Cleaned.csv', index = False)





















