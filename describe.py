#step -1 sample data frame 

import pandas as pd

data = {
    "Name" : ['vishal','Vivek','vaibhav'],
    "Age" : [20, 22, 24],
    "City" : ['nagpur', 'kanpur','sikandarpur'],

}

df = pd.DataFrame(data)
print("Sample DataFrame")
print(df)
print('Descriptive statistics')
print(df.describe())