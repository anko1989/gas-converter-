import streamlit as st
import pandas as pd

# ===== PAGE CONFIG (WAJIB paling atas) =====
st.set_page_config(layout="centered")

# ===== STYLE (center box) =====
st.markdown("""
    <style>
        .main {
            max-width: 700px;
            margin: auto;
        }
    </style>
""", unsafe_allow_html=True)

# ===== LOAD DATA =====
data = pd.read_csv('dewpoint_data.csv', encoding='latin-1')
data = data.dropna(axis=1, how='all')
data["DEWPOINT °C @ 1 Bar"] = data["DEWPOINT °C @ 1 Bar"].astype(float)

# ===== FUNCTION =====


def dewpoint_converter(dp_input):
    closest = data.iloc[(data["DEWPOINT °C @ 1 Bar"] -
                         dp_input).abs().argsort()[:1]]
    return closest.iloc[0]


# ===== TITLE =====
st.markdown("<h1 style='text-align: center;'>Santong DP Converter</h1>",
            unsafe_allow_html=True)

# ===== INPUT BOX =====
st.markdown("### Enter Dewpoint (°C)")
dp_input = st.number_input("", value=-90.0)

convert_btn = st.button("Convert")

# ===== RESULT =====
if convert_btn:
    result = dewpoint_converter(dp_input)

    st.markdown("## Result")

    col1, col2 = st.columns(2)

    for i, col in enumerate(result.index):
        if "Unnamed" not in col:
            if i % 2 == 0:
                col1.write(f"**{col}**: {result[col]}")
            else:
                col2.write(f"**{col}**: {result[col]}")
