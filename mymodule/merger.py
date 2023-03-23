import pandas as pd

customers=pd.read_excel("C://mydatasets//hclorders.xlsx",sheet_name="customers")
orders=pd.read_excel("C://mydatasets//hclorders.xlsx",parse_dates=["order_date"],sheet_name="orders")
products=pd.read_excel("C://mydatasets//hclorders.xlsx",sheet_name="products")
result=pd.merge(left=customers,right=orders,on="cust_id",how="inner")
result1=pd.merge(left=orders,right=products,on="order_id",how="left")
result2=pd.merge(left=result,right=result1,on="order_id",how="left")
print(result2)
r=pd.concat([customers,orders],axis=0)
print(r)