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

        colA, colB = st.columns(2)

        for i, col in enumerate(result.index):
            if "Unnamed" not in col:
                if i % 2 == 0:
                    colA.write(f"**{col}**")
                    colA.write(result[col])
                else:
                    colB.write(f"**{col}**")
                    colB.write(result[col])
