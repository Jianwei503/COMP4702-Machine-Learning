import pandas as pd

# dataframe[column (series)] [row (Series index)]
data_set = pd.read_csv('penguins_raw.csv')
# columns indices to be extracted, start from 0
col_wanted = [2, 4, 7, 9, 10, 11, 12, 13, 14, 15]
# extract needed columns
data = data_set.iloc[:, col_wanted]

rows_num = len(data)
col_num = len(data.columns)

# replace nominal values with numeric values
for i in range(rows_num):
    if data.at[i, 'Species'] == 'Adelie Penguin (Pygoscelis adeliae)':
        data.at[i, 'Species'] = 1
    elif data.at[i, 'Species'] == 'Gentoo penguin (Pygoscelis papua)':
        data.at[i, 'Species'] = 2
    else:
        data.at[i, 'Species'] = 3

for i in range(rows_num):
    if data.at[i, 'Island'] == 'Torgersen':
        data.at[i, 'Island'] = 1
    elif data.at[i, 'Island'] == 'Biscoe':
        data.at[i, 'Island'] = 2
    else:
        data.at[i, 'Island'] = 3

for i in range(rows_num):
    if data.at[i, 'Clutch Completion'] == 'Yes':
        data.at[i, 'Clutch Completion'] = 1
    else:
        data.at[i, 'Clutch Completion'] = 0

for i in range(rows_num):
    if data.at[i, 'Sex'] == 'MALE':
        data.at[i, 'Sex'] = 1
    elif data.at[i, 'Sex'] == 'FEMALE':
        data.at[i, 'Sex'] = 2
    else:
        data.at[i, 'Sex'] = None

# drop the rows where at least one element is missing.
data = data.dropna()

data.to_csv('penguins_raw_pca.csv', header=None, index=False)
print ('done')


