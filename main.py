import pandas as pd
import os

# print("Current directory:", os.getcwd())
df = pd.read_csv("PriceSheet/Residential.csv")

#                               Rows   Col
Qcell415_Row0_6_13 = df.iloc[[0,6,13],0:19] 
#                                     ^^  obtains the first 19, 0:18

## _______________ Helpful CODE ref. .shape .size .dtypes 
# print("\nUsing .size to get the total elements, here its ( Rows )x ( Col ) here its 3 x 19 =", Qcell415_Row0_6_13.size)
# print("\nUsing the .shape function to obtain the ROWS and COLS, this is returned as a tuple: ", Qcell415_Row0_6_13.shape)
# [rowOfData,colOfData] = Qcell415_Row0_6_13.shape
# print("I used two variables to capture the tuple\nROWS: ", rowOfData, "COL: ", colOfData)
# print("\nUsing .dtypes - to ouptupt our current dataFrame's  col NAME and its dataTYPE\nThis comes out as a series listing: 🌊 ", Qcell415_Row0_6_13.dtypes)

# print(Qcell415_Row0_6_13.head())
qty415 = Qcell415_Row0_6_13.iloc[1]
Qcell415_Row0_6_13.columns = qty415

print(Qcell415_Row0_6_13.head())

Qcell415_Row0_6_13 = Qcell415_Row0_6_13.drop(Qcell415_Row0_6_13.index[1])
Qcell415_Row0_6_13 = Qcell415_Row0_6_13.drop(Qcell415_Row0_6_13.index[0])
Qcell415_Row0_6_13 = Qcell415_Row0_6_13.drop(Qcell415_Row0_6_13.columns[-1], axis=1)
# Qcell415_Row0_6_13.index = ['Qcell415', 'Total Cost']
Qcell415_Row0_6_13 = Qcell415_Row0_6_13.reset_index(drop=True)
Qcell415_Row0_6_13 = Qcell415_Row0_6_13.rename(columns={'Qty. PV Modules': 'Qcell415'})


print("try")
print(Qcell415_Row0_6_13.head())

# make an array the exact col size of the data
# Qcell415_count = pd.DataFrame({ 'qty415': range(1,colOfData)})





lg375_Row = df.iloc[20:25,0:19] 