import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('winequality-red.csv',sep=';')
# 欠損値なし

x = df.drop('quality',axis=1)
# 説明変数
y = df['quality']
# 目的変数

model = LinearRegression()
model.fit(x,y)

print('切片:',model.intercept_)
print('係数:',model.coef_)

