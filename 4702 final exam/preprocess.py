import pandas as pd

# dataframe[column (series)] [row (Series index)]
data = pd.read_csv('penguins_raw.csv')

data.to_csv('penguins_raw.csv', index=False)
print ('done')

