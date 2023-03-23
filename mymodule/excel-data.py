import pandas as pd
df=pd.read_excel("c://mydatasets//sample_pivot.xlsx",sheet_name='Sheet1')
task1=pd.crosstab(index=df['Region'],columns=df['Type'],values=df['Sales'],aggfunc='mean')
task2=pd.crosstab([df.Region,df.Date.dt.quarter],df.Type,values=df.Sales,margins=True,aggfunc='sum')
print(task1)
print(task2)
print (df)