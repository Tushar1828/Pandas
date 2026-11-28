import pandas as pd 

data ={
     "Name": ['Arun','Varun','Karan','Tushar','vishal','vivek'],
     "Age":[28,34,22,34,28, 30],
     "Salary":[50000,56000,67000,83000,57000,19999]

}
df = pd.DataFrame(data)
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)