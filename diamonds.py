import pandas as pd
import numpy as np

df=pd.read_csv(r'/Users/ASUS/OneDrive/AIO PYTHON/python project 1/diamonds.csv')

print (df.head(10))# first 10 rows.
print()

#cal total value of all diamonds
sum=df.price.sum()
print('total $value of all diamond:${:0,.2f}'.format(sum))

#last 10 rows of all diamond.
print('last 10 rows of all diamond')
print(df.tail(10))
print()
