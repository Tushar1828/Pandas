# Employee Salary Analysis
# Scenario: A company has 1,000 employees. HR wants to find employees whose salary is greater than ₹50,000.

# import pandas as pd

# data = {
#     'Name': ['Amit', 'Rahul', 'Tushar', 'Priya', 'Rohit'],
#     'Department': ['IT', 'HR', 'IT', 'Sales', 'HR'],
#     'Salary': [45000, 60000, 75000, 40000, 55000]
# }

# df = pd.DataFrame(data)

# result = df[df['Salary'] > 50000]

# print(result)

# How do you merge two DataFrames?
# import pandas as pd

# df1 = pd.DataFrame({
#     'ID': [1, 2],
#     'Name': ['Amit', 'Rahul']
# })

# df2 = pd.DataFrame({
#     'ID': [1, 2],
#     'Salary': [30000, 40000]
# })

# result = pd.merge(df1, df2, on='ID')

# print(result)

# Customers Who Spent More Than ₹10,000

import pandas as pd

data = {
    'Customer': ['A', 'B', 'C', 'D'],
    'Amount': [4900, 17000, 56000, 67000]
}

df = pd.DataFrame(data)

result = df[df['Amount'] > 10000]
print(result)