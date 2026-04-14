import streamlit as st
import pandas as pd

# ===== PAGE CONFIG (WAJIB paling atas) =====
st.set_page_config(layout="wide")

# ===== LOAD DATA =====
data = pd.read_csv('dewpoint_data.csv', encoding='latin-1')
data = data.dropna(axis=1, how='all')
data["DEWPOINT °C @ 1 Bar"] = data["DEWPOINT °C @ 1 Bar"].astype(float)


def dewpoint_converter(dp_input):
    closest = data.iloc[(data["DEWPOINT °C @ 1 Bar"] -
                         dp_input).abs().argsort()[:1]]
    return closest.iloc[0]


# ===== 2 COLUMN LAYOUT =====
left, right = st.columns([1, 2])  # kiri kecil, kanan besar

# ===== LEFT SIDE =====
with left:
    st.title("Santong DP Converter")
    st.markdown("### Enter Dewpoint (°C)")

    dp_input = st.number_input("", value=-90.0)
    convert_btn = st.button("Convert")

# ===== RIGHT SIDE =====
with right:
    st.markdown("## Result")

    if convert_btn:
        result = dewpoint_converter(dp_input)

        for col in result.index:
            if "Unnamed" not in col:
                st.write(f"**{col}**: {result[col]}")
