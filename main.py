import pandas as pd
import os

# print("Current directory:", os.getcwd()) #Gets current directory
df = pd.read_csv("PriceSheet/Residential.csv")

#                               Rows   Col
Qcell415_Row0_6_13 = df.iloc[[0,6,13],0:20] 
#                                     ^^  obtains the first 19, 0:18

## _______________ Helpful CODE ref. .shape .size .dtypes 
# print("\nUsing .size to get the total elements, here its ( Rows )x ( Col ) here its 3 x 19 =", Qcell415_Row0_6_13.size)
# print("\nUsing the .shape function to obtain the ROWS and COLS, this is returned as a tuple: ", Qcell415_Row0_6_13.shape)
# [rowOfData,colOfData] = Qcell415_Row0_6_13.shape
# print("I used two variables to capture the tuple\nROWS: ", rowOfData, "COL: ", colOfData)
# print("\nUsing .dtypes - to ouptupt our current dataFrame's  col NAME and its dataTYPE\nThis comes out as a series listing: 🌊 ", Qcell415_Row0_6_13.dtypes)


# the following two lines of code allow me to rename the columns 
qty415 = Qcell415_Row0_6_13.iloc[1] # taking the second ROW
Qcell415_Row0_6_13.columns = qty415
# using the pandas attribute .columns 
# .columns holds all column names of my current DataFrame

# I don't want doubles or other sections of this 
Qcell415_Row0_6_13 = Qcell415_Row0_6_13.drop(Qcell415_Row0_6_13.index[1])
Qcell415_Row0_6_13 = Qcell415_Row0_6_13.drop(Qcell415_Row0_6_13.index[0])
Qcell415_Row0_6_13 = Qcell415_Row0_6_13.drop(Qcell415_Row0_6_13.columns[-1], axis=1) # removes the last column 
# second to last step in cleaning is re setting the rows
Qcell415_Row0_6_13 = Qcell415_Row0_6_13.reset_index(drop=True)
# last step, I like to remane my column...
Qcell415_Row0_6_13 = Qcell415_Row0_6_13.rename(columns={'Qty. PV Modules': 'Qcell415'})

print(Qcell415_Row0_6_13.head())



lg375 = df.iloc[[25,28,35],0:19] 
lg375QTY = lg375.iloc[1]
lg375.columns = lg375QTY
lg375 = lg375.drop(lg375.index[[0,1]])
lg375 = lg375.reset_index(drop=True)
lg375 = lg375.rename(columns={'Qty. PV Modules': 'LG375'})
print(lg375.head())

# filtered = df[df.apply(lambda row: row.astype(str).str.contains('Qty. PV Modules ', case=False).any(), axis=1)]
filtera = df[df.apply(lambda row: row.astype(str).str.contains('Module|Cost Per Watt|System Size|Total Cost of PV System|Qty. PV Modules', case=False).any(), axis=1)]
print(filtera)
