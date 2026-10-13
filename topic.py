import pandas as pd

data = {
    "Name" : ['vishal','Vivek','vaibhav'],
    "Age" : [20, 22, 24],
    "City" : ['nagpur', 'kanpur','sikandarpur'],
    "Salary" : [45000,53000,32000],
    "Performance" : [67,84,45,]
    
}

df = pd.DataFrame(data)
print(f'Shape: {df.shape}')
print(f'Column Names: {df.columns}')
      