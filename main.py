import pandas as pd
df=pd.read_csv('bestsellers.csv')
print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())