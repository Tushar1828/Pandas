import pandas as pd

data = {
    "Name" : ['vishal','Vivek','vaibhav'],
    "Age" : [20, 22, 24],
    "City" : ['nagpur', 'kanpur','sikandarpur'],
}

df = pd.DataFrame(data)
print(df)
