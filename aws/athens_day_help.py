import pandas as pd

pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 400)
pd.set_option('max_colwidth', 800)
pd.set_option('display.max_rows', None)

df = pd.read_csv('Combined_table_athens_day.csv')

new_df = df.iloc[:, [2, 5, 6, 13, 14, 15, 16, 17]]

print(new_df)