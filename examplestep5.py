import pandas as pd

data = {
    "Name" : ['vishal','Vivek','vaibhav'],
    "Age" : [20, 22, 24],
    "City" : ['nagpur', 'kanpur','sikandarpur'],
    "Salary" : [45000,53000,32000],
    "Performance" : [67,84,45,]
}

df = pd.DataFrame(data)

#display the datafRAME
print("Sample DataFrame")
print(df)
print("Names (single column return series)")
name = df['Name']
print(name)

#selecting multiple columns
subset = df[["Name", "Salary"]]
print('\nSubset with Name and salary')
print(subset)