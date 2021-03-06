# -*- coding: utf-8 -*-
"""Stock_Price_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15edgFcwC0SHqgGcc1uPVbLoJDkv4iFTl
"""

import os
os.environ['KAGGLE_USERNAME'] = "dwivediabhishek1998"
os.environ['KAGGLE_KEY'] = "1f1a04f5e87a8393dbc1f82a387dcfac"

!kaggle datasets download -d rpaguirre/tesla-stock-price

from zipfile import ZipFile

with ZipFile('/content/tesla-stock-price.zip', 'r') as zipObj:
   zipObj.extractall()

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/Tesla.csv - Tesla.csv.csv')
df.describe(include='all')

df.dtypes

df['Date'] = pd.to_datetime(df['Date'])

df.dtypes

df = df.drop('Volume', axis=1)
df = df.drop('Adj Close', axis=1)
y = df['Close']
x = df.drop('Close', axis=1)

x.head()

y.head()

train = df[0:1200]
valid = df[1200:]

x_train = train.iloc[:,[1,2,3]]
y_train = train.iloc[:,4]
date_train=train.iloc[:,0]
x_valid = valid.iloc[:,[1,2,3]]
y_valid = valid.iloc[:,4]
date_valid=valid.iloc[:,0]

f, ax = plt.subplots(1, 1, figsize = (20, 10))
ax.plot(date_train, y_train, color = 'red', linewidth='0.75')
ax.plot(date_valid, y_valid, color = 'blue', linewidth='0.75')
plt.show()

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(x_train,y_train)
pred = reg.predict(x_valid)

f, af = plt.subplots(1, 1, figsize = (20, 10))
# af.plot(date_train, y_train, color = 'red', linewidth='0.75')
af.plot(date_valid, y_valid, color = 'blue',linewidth='1')
af.plot(date_valid, pred, color='green', marker='o', linewidth=0.5)
plt.show()

x_valid.values[0,:]

prediction = reg.predict([[202.509995, 205.059998, 201.139999]])

original = y_valid.values[0]

print('original: ', original , 'and predicted: ', prediction[0])

"""The predicted and given values are almost same"""

