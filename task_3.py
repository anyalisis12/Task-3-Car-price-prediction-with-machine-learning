# -*- coding: utf-8 -*-
"""Task 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ep0zY9QQi60OXSEs2L7bYsTgIbP4r5Kg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel('/content/datadictionary.xlsx')
data

df = pd.read_csv('/content/Cars.csv')
df

df.head()

df.shape

df.drop_duplicates(inplace=True)

df.shape

df.info()

"""Data Preprocessing"""

df_cat = ['Name','Location','Fuel_Type','Transmission','Owner_Type','Colour']

for col in df_cat:
    print(col.upper(),":",df[col].nunique())
    print(df[col].value_counts().sort_values(ascending=False))
    print('\n')

df.drop('Name',axis=1,inplace=True)

df['Mileage'] = df['Mileage'].str.replace('[a-zA-Z/]', '',regex=True)
df['Mileage'] = df['Mileage'].astype('float')

df['Power'] = df['Power'].str.replace('[a-zA-Z/ ]', '',regex=True)
df['Power'].replace('',np.nan,inplace=True)

df['Power'] = df['Power'].astype('float')

df.info()

"""Checking percentage of missing values"""

df['New_Price'].isnull().sum()

for i in df.columns:
    print('Precentage of missing values is {} % in {} '.format(round(
        (df[i].isnull().sum()/df.shape[0])*100,2),i))

df.drop('New_Price',axis=1,inplace=True)

for col in df.select_dtypes(exclude='object'):
    df[col] = df[col].replace(np.nan,df[col].median())

df.isnull().sum()

df.dropna(inplace=True)

df.shape

df.info()

df.isnull().sum()

for col in df.select_dtypes(include='object'):
    print(df[col].value_counts())
    print('\n')

df.head(10)

"""Checking descriptive Stats of the data
1. Chechking the descriptive stats(5 pt summary i.e, min,max,25%,50%,75%)
2. Comparing mean and median (to check if there are any outliers present in a column)
3. If there are any categorical columns check the number of unique values present and check its top and frequency.
"""

df.describe(include='all').T

df[df['Mileage']==0]

df[df['Engine']==72]

df = df.drop(df[df['Engine'] == 72].index)
df[df['Engine']==72]

df.shape

df.columns