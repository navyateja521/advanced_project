import pandas as pd
df=pd.read_excel("C://mydatasets//Arrival_Dates.xlsx",sheet_name="Sheet1")
df1=pd.read_excel("C://mydatasets//Arrival_Dates_Final.xlsx",sheet_name="Sheet1")
result=df.compare(df1,align_axis=1)
result1=df.compare(df1,keep_equal=False)
result1.to_excel("C://mydatasets//result.xlsx")
print(result)
print(result1)

