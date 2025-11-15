import pandas as pd

data = pd.DataFrame({'tits': range(6,0,-1),
                     'brains': ['1', '3','22','35','127','666'],
                     'brawn':['PHY', 'MAT', 'CAL', 'CSS', 'EGN', 'SIX']})
print(data)

# get this specific row indice 

singleList = data['brains'].tolist() # accessing by column name
print(singleList)
print("the class type of the column - brains is of type: ", type(singleList))