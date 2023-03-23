import pandas as pd

df=pd.read_csv(filepath_or_buffer='c://mydatasets//tips.csv')
# gender_tips=df.loc[df['sex']== 'Female']
# print(gender_tips)
# print(df)
smoker_sex=df.groupby(['smoker','sex'])['smoker'].count()
print(smoker_sex)
df['mes']=df['size'].apply(lambda x:"large" if x>=3 else "small")
print(df)

