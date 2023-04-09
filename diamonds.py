import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv(r'/Users/ASUS/OneDrive/AIO PYTHON/python project 1/diamonds.csv')

print (df.head(10))# first 10 rows.
print()

#last 10 rows of all diamond.
print('last 10 rows of all diamond')
print(df.tail(10))
print()

#cal total value of all diamonds
sum=df.price.sum()
print('total $value of all diamond:${:0,.2f}'.format(sum))

#calculating mean price of diamonds from all diamond.
mean=df.price.mean()
print('mean  of all diamond:${:0,.2f}'.format(mean))

#summarize the data
descrip=df.carat.describe()
print()
print(descrip)

descrip=df.describe(include='object')
print()
print(descrip)

# looking at shiny diamonds
carat=df.carat
clarity=df.clarity
plt.scatter(clarity,carat)
plt.show()

# no of diamonds in each clarity type
# count the number of each textual clarity type
clarityindexes=df['clarity'].value_counts().index.tolist()
claritycount=df['clarity'].value_counts().values.tolist()
print(clarityindexes)
print(claritycount)
plt.bar(clarityindexes,claritycount)
plt.show()