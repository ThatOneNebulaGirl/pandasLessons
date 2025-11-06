# import pandas as pd
# df = pd.read_csv("BFSE Q3 2024 Price Sheet/Residential-Table 1.csv")
# print(df.head())
import pandas as pd
import os

print("Current directory:", os.getcwd())
df = pd.read_csv("PriceSheet/Residential.csv")

# # Correct relative path (no leading slash)
# df = pd.read_csv("PriceSheet/Residential.csv")

# df.column.value[0] = id

# print(df.iloc[6])
# print(df.head(15))


Qcell415_Row0_6_13 = df.iloc[[0,6,13],]
# print(df.iloc[6])
# print(Qcell415_Row0_6_13.head(3))
print(Qcell415_Row0_6_13.iloc[:, 4:11])


