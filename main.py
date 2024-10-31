import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv", encoding="ISO-8859-1")
print(df.columns)
df['Age'].plot(kind='line', title='Bar Plot')
plt.xlabel('Categorical Column')
plt.ylabel('Average of Numerical Column')
plt.savefig("a.png")
# print(df.head())

