import pandas as pd

data = {
    "Name" : ['vishal','Vivek','vaibhav'],
    "Age" : [20, 22, 24],
    "City" : ['nagpur', 'kanpur','sikandarpur'],
    "Salary" : [45000,53000,32000],
    "Performance" : [67,84,45,]
}

df = pd.DataFrame(data)

high_Salary = df[df['Salary'] > 50000]
print('Employees with Salary > 50000')
print(high_Salary) 

#filtering rows salary > 50k & age > 30
filtered  = df[(df['Age'] > 30) & (df['Salary']> 50000)]
print(f'Employee list Age > 30 + Salary > 50000')
print(filtered )