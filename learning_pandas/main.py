import pandas as pd

data = {
    "Name" : ['vishal','Vivek','vaibhav'],
    "Age" : [20, 22, 24],
    "City" : ['nagpur', 'kanpur','sikandarpur'],
}

df = pd.DataFrame(data)
print(df)

# df.to_csv("ouput.csv", index=False)
# df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)
   