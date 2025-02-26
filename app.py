import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/RalfsKanders/skateboard-trick-dashboard/main/dataset.csv"

try:
    df = pd.read_csv(url)
    st.write("Skateboarding Olympic Games Data", df)


    country = st.selectbox("Select Country", df["Country"].unique())
    filtered_data = df[df["Country"] == country]
    st.write(f"Data for {country}:")
    st.write(filtered_data)


    medal_counts = df["Medal"].value_counts()
    st.bar_chart(medal_counts)
except Exception as e:
    st.error(f"Error loading dataset: {e}")
