import pandas as pd

data=pd.read_csv("data.csv")

print(f"First Five Rows: \n {data.head()}")
print(f"Last Five Rows: \n {data.tail()}")
print(f"Data Info: \n {data.info()}")
print(f"Data description: \n {data.describe()}")

age=data["Age"]
print(f"Single Col: \n {age}")

df=data[["Age","Score"]]
print(f"Multiple Col: \n {df}")

score=data[data["Score"]>80]
print(f"Filtered Rows (Score>80): \n {score}")