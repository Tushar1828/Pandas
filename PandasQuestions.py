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

# import pandas as pd

# data = {
#     'Customer': ['A', 'B', 'C', 'D'],
#     'Amount': [4900, 17000, 56000, 67000]
# }

# df = pd.DataFrame(data)

# result = df[df['Amount'] > 10000]
# print(result)

# Calculate Profit and Loss
# import pandas as pd

# data = {
#     'Product': ['Laptop', 'Mobile', 'Tablet'],
#     'Selling_Price': [60000, 25000, 30000],
#     'Cost_Price': [45000, 20000, 28000]
# }

# df = pd.DataFrame(data)

# df['Profit'] = (
#     df['Selling_Price'] - df['Cost_Price']
# )
# print(df)

# the difference between consecutive transactions.
# import pandas as pd


# df = pd.DataFrame({
#     'Amount': [1000, 1500, 1200, 2000, 2500]
# })

# df['Difference'] = df['Amount'].diff()

# print(df)


# the top two employees in each department based on salary.

# import pandas as pd


# df = pd.DataFrame({
#     'Name': ['A', 'B', 'C', 'D', 'E', 'F'],
#     'Department': ['IT', 'IT', 'IT', 'HR', 'HR', 'HR'],
#     'Salary': [30000, 50000, 40000, 25000, 45000, 35000]
# })

# result = df.sort_values(
#     'Salary',
#     ascending=False
#     ).groupby('Department').head(2)

# print(result)

# customers who purchased more than twice

# import pandas as pd

# df = pd.DataFrame({
#     'Customer': ['Amit', 'Rahul', 'Amit', 'Priya',
#                  'Rahul', 'Amit', 'Tushar', 'Rahul'],
#     'Amount': [1000, 2000, 1500, 3000,
#                2500, 4000, 1200, 3500]
# })

# # result = df['Customer'].value_counts()

# # print(result[result > 2])
# result = df.groupby('Customer').filter(
#     lambda x: len(x) > 2
# )

# print(result)


# employees with salaries above the company average

# import pandas as pd

# df = pd.DataFrame(
#     {
#     'Name': ['Amit', 'Rahul', 'Priya', 'Tushar'],
#     'Salary': [30000, 50000, 40000, 70000]
# })

# avg = df['Salary'].mean()

# result = df[df['Salary'] > avg]

# print(result)

# customers who made exactly 2 purchases.

import pandas as pd

df = pd.DataFrame({
    'Customer': ['A', 'B', 'A', 'C', 'B', 'A']
})

counts = df['Customer'].value_counts()

print(counts[counts == 2])