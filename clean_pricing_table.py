from data_cleaning_utils import load_resident_pricing, extract_lg375


def main():
    df = load_resident_pricing()
    lg375 = extract_lg375(df)

    print("LG375 cleaned pricing table: ")
    print(lg375.head())

if __name__ == "__main__":
    main()