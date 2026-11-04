# Employee Salary Analysis
# Scenario: A company has 1,000 employees. HR wants to find employees whose salary is greater than ₹50,000.

import pandas as pd

data = {
    'Name': ['Amit', 'Rahul', 'Tushar', 'Priya', 'Rohit'],
    'Department': ['IT', 'HR', 'IT', 'Sales', 'HR'],
    'Salary': [45000, 60000, 75000, 40000, 55000]
}

df = pd.DataFrame(data)

result = df[df['Salary'] > 50000]

print(result)