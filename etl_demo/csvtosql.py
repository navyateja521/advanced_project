import pandas as pd
from sqlalchemy import create_engine
db_connection_str= 'mysql+pymysql://navya:navya teja@localhost/myhcl'
db_connection = create_engine(db_connection_str)
df=pd.read_excel("c://mydatasets//sample_pivot.xlsx",sheet_name='Sheet1')
# task1=pd.crosstab(index=df['Region'],columns=df['Type'],values=df['Sales'],aggfunc='mean')
# task2=pd.crosstab([df.Region,df.Date.dt.quarter],df.Type,values=df.Sales,margins=True,aggfunc='sum')
# print(task1)
# print(task2)
# print (df)
# try:
#     df.to_sql(name="mytable",con=db_connection)
# except Exception as e:
#     print(e)
cp=df.copy()
# print(df.isna().sum())
df.fillna(0,inplace=True)
# print(df)
print(df.isna().sum())