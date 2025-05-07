import pandas as pd


df_excel = pd.read_excel('list.xlsx')

str = int(input('Введите номер строки: '))
print(df_excel.iloc[str])