import pandas as pd

df = pd.DataFrame(
    {
        "Name" : ["john", "robert", "angel"],
        "Age": [19, 32, 21],
        "Origin": ['France', "US", "UK"]
    }
)

#print(df)
print()
#print(list(df.columns))
#print(df["Origin"])
#print(df["Age"])

#weight = pd.Series([180, 165, 230], name="weight")
print(df)