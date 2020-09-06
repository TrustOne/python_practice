import pandas as pd


df = pd.read_excel('g:/python/section2/python_practice/files/excel_s1.xlsx',na_values='...',converters={"2003":lambda w: w if w > 60000 else None})


df['State'] = df['State'].str.replace(' ','|')
# print(df)

df['Avg'] = df[['2003','2004','2005']].mean(axis=1).round(2)

df['Sum'] = df[['2003','2004','2005']].sum(axis=1).round(2)


print(df)
df.to_excel('g:/python/section2/python_practice/files/result_s1.xlsx')
