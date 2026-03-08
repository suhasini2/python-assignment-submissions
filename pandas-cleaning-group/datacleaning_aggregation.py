import pandas as pd
import numpy as np

data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

#detect missing values
print(df.isnull().sum())

#calculate mean salary
meansalary=df["Salary"].mean()

#filling mean value in Nan value
df["Salary"]=df["Salary"].fillna(meansalary)

#dropping table
df1=df.drop(columns="Temporary_Notes")

#rename table
df2=df.rename(columns={"Salary":"Annual_Salary"})

#groupby 'Department' and calculate mean on salary and count Employee and rename the col names
df3=df2.groupby("Department").agg(Average_Salary=("Annual_Salary","mean"), Employee_Count=("Employee","count"))
print(df3)

