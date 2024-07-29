import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv(r"C:\Users\visha\Downloads\milk-tea-coffee (2).csv")
df = pd.DataFrame(data)
print(df.values)

# plt.boxplot(df['Year'], df['Milk'])
# plt.show()