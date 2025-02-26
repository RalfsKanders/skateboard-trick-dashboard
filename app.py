import streamlit as st
import pandas as pd



def load_data():
    url = "https://raw.githubusercontent.com/RalfsKanders/skateboard-trick-dashboard/main/dataset.csv"

    df = pd.read_csv(url)

    return df


df = load_data()

st.title("Skateboard Trick Classification")
st.write("Here is the dataset of skateboard tricks:")

st.dataframe(df)

