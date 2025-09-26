import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold,cross_val_score

df = pd.read_csv('winequality-red.csv',sep=';')


des = df.drop('quality',axis=1).describe()

# 説明変数の統計量

Q1 = des.loc['25%']
# 第一四分位数
Q3 = des.loc['75%']
# 第三四分位数
IQR = Q3 - Q1
# 四分位範囲

lower = IQR * 1.5 - Q1
upper = IQR * 1.5 + Q3
# 外れ値の下限、上限

columns = df.drop('quality',axis=1).columns

for col in columns:
    df = df[(df[col] >= lower[col]) & (df[col] <= upper[col])]
# 外れ値を除外    

x = df.drop('quality',axis=1)
y = df['quality']

model = LinearRegression()

kf = KFold(n_splits=5,shuffle=True,random_state=42)

scores = cross_val_score(model,x,y,cv=kf,scoring='r2')

print('各分割における決定係数:', scores)
print('交差検証の平均決定係数:', scores.mean())
   


