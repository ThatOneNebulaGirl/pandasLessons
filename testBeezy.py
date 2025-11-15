import pandas as pd
import os

# df = pd.read_csv("PriceSheet/Residential.csv")
arr = dir(pd)
s = pd.Series(arr)
print(s)


print("\nbleh")
# GOAL - to categorize all attributes and functions inside the pandas module itself
## I would like to come back to this code and make a ML model that groups common groups together.
## tbh i currently don't know how I'm gonna pull this off. but! Idea #1 - same word. 
## idea #2 - group POSSIBLE commonalities ? such as single word commands? like abs and add are both single words
## and maybe the same? (obvi i know) but if I didn't how could I find out?? 
## idea #2.1 get python to talk to online dictonary ?? <- this a thing? okay say it is. 
## then we do a char def check... like abs and add will have words relative to MATH... 