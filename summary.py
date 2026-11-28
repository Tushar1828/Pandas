"""df["column Name"].mean()
df["Column Name"].sum()
df["Column Name"].min()
df["Column Name"].max()"""

import pandas as pd 

data ={
     "Name": ['Arun','Varun','Karan'],
     "Age":[28,34,22],
     "Salary":[1000,2000,3000]

}
df = pd.DataFrame(data)

avg_salary = df['Salary'].mean()
print(avg_salary)