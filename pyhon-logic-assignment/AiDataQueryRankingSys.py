import pandas as pd

df=pd.read_csv("aidata.csv")

#Single row
print(df["Name"])

#multiple row
data=df[["Name","Passed","Category"]]

#labeling
df.index=['r1','r2','r3','r4','r5']

#accessing data by iloc
print(df.iloc[0])

#accessing data by loc
print(df.loc['r2'])

#Filtering score>80
score=df[df["Score"]>80]

#filtering score>80 and Passes is true and sorting in descnding order
result=df[(df["Score"]>80) & (df["Passed"]==True)].sort_values(by="Score",ascending=False)
print(result)


