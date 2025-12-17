import pandas as pd

# def loading function
def load_resident_pricing(csv_path="PriceSheet/Residential.csv"):
    return pd.read_csv(csv_path)

def extract_lg375(df):
    lg375 = df.iloc[[25,28,35], 0:19]

    lg375_qty = lg375.iloc[1]
    lg375.columns = lg375_qty

    lg375 = lg375.drop(lg375.index[[0,1]])
    lg375 = lg375.reset_index(drop=True)
    lg375 = lg375.rename(columns={'Qty. PV Modules': 'LG375'})

    lg375.columns.name = None 

    return lg375

# df = load_resident_pricing()
# lg375 = extract_lg375(df)

# print(lg375.head())
