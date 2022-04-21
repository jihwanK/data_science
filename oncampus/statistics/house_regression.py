#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import sklearn as skl
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_excel('apartment_deals_price.xlsx', 'Sheet1')

'''
fig, axs = plt.subplots(figsize=(16,8) , ncols=3, nrows=2)
features = ['size', 'contract_month', 'contract_day', 'floor', 'built_year']
for i, feature in enumerate(features):
	row = int(i/3)
	col = i%3
	sns.regplot(x=feature, y='price', data=df, ax=axs[row][col])
'''

###############################################################################

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score

y_target = df['price']
X_data = df.drop(['price', 'area', 'building_number', 'apartment_name', 'address'], axis=1, inplace=False)

X_train , X_test , y_train , y_test = train_test_split(X_data, y_target, test_size=0.3, random_state=156)

lr = LinearRegression()
lr.fit(X_train, y_train)
y_preds = lr.predict(X_test)
mse = mean_squared_error(y_test, y_preds)
rmse = np.sqrt(mse)

print('MSE : {0:.3f} , RMSE : {1:.3F}'.format(mse , rmse))
print('Variance score : {0:.3f}'.format(r2_score(y_test, y_preds)))

###############################################################################

import math

coeff = pd.Series(data=np.round(lr.coef_, 2), index=X_data.columns)
coeff.sort_values(ascending=False)

coeff.sort_values(ascending=False, inplace=True)
res = 'price = '
for idx, item in enumerate(coeff.items()):
	name, value = item
	if idx == 0:
		op = ''
	else:
		if value > 0:
			op = ' + '
		else:
			op = ' - '
	res += op + '*'.join([str(math.fabs(value)), name])

if lr.intercept_ > 0:
	res += " + " + str(math.fabs(lr.intercept_))
else:
	res += " - " + str(math.fabs(lr.intercept_))

print()

print('[Linear regression]')
print(res)

print()

print('[Covariance of all variables in terms of price]')
print(df.cov()['price'])

print()

print('[Sorted covariance of all variables in terms of price]')
df.cov()['price'][df.cov()['price'].abs().sort_values(ascending=False).keys()]
