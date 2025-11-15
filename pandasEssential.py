import pandas as pd
import numpy as np

#https://pandas.pydata.org/docs/user_guide/basics.html

index = pd.date_range("1/1/1990", periods=8)
s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=["A", "B", "C"])

long_series = pd.Series(np.random.randn(1000))

print(long_series.head())