import pandas as pd
import streamlit as st

# Load data
data = pd.read_csv('dewpoint_data.csv', encoding='latin-1')
data = data.dropna(axis=1, how='all')
data["DEWPOINT °C @ 1 Bar"] = data["DEWPOINT °C @ 1 Bar"].astype(float)

st.title("Santong DP Converter")

# Input
dp_input = st.number_input("Enter Dewpoint (°C):", value=-90.0)

# Button
if st.button("Convert"):
    closest = data.iloc[(data["DEWPOINT °C @ 1 Bar"] -
                         dp_input).abs().argsort()[:1]]
    row = closest.iloc[0]

    st.subheader("Result")

    for col in row.index:
        if "Unnamed" not in col:
            st.write(f"{col}: {row[col]}")
