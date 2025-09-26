import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold,cross_val_score

df = pd.read_csv('winequality-red.csv',sep=';')

x = df.drop('quality',axis=1)
y = df['quality']

model = LinearRegression()

kf = KFold(n_splits=5,shuffle=True,random_state=42)

scores = cross_val_score(model,x,y,cv=kf,scoring='r2')

print('各分割における決定係数:',scores)
print('平均決定係数:',scores.mean())
