import pandas as pd

# Load data
data = pd.read_csv('dewpoint_data.csv', encoding='latin-1')
data = data.dropna(axis=1, how='all')

# Convert column ke float
data["DEWPOINT °C @ 1 Bar"] = data["DEWPOINT °C @ 1 Bar"].astype(float)

# Function converter


def dewpoint_converter(dp_input):
    closest = data.iloc[(data["DEWPOINT °C @ 1 Bar"] -
                         dp_input).abs().argsort()[:1]]
    return closest.iloc[0]


# TEST dulu
if __name__ == "__main__":
    dp = float(input("Enter dewpoint: "))
    result = dewpoint_converter(dp)

    print("\n=== RESULT ===")
    for col in result.index:
        if "Unnamed" not in col:
            print(f"{col}: {result[col]}")
