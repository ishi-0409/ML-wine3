import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('winequality-red.csv',sep=';')

x = df.drop('quality',axis=1)

for col in x.columns:
    sns.boxenplot(y=x[col])
    plt.ylabel(col)
    plt.show()
    