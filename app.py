import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Skateboarding Trick Classification Dashboard")

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/RalfsKanders/SkateboardML/main/skateboard_tricks.csv"
    df = pd.read_csv(url)
    return df

df = load_data()

st.subheader("Dataset Preview")
st.write(df.head())

st.subheader("Dataset Summary")
st.write(df.describe())

st.subheader("Trick Frequency Distribution")
fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(y=df['trick_name'], order=df['trick_name'].value_counts().index, ax=ax, palette="coolwarm")
ax.set_title("Most Common Tricks")
st.pyplot(fig)

st.subheader("Success Rate of Tricks")
if "success" in df.columns:
    fig, ax = plt.subplots(figsize=(6, 4))
    df["success"].value_counts().plot(kind="bar", color=["green", "red"], ax=ax)
    ax.set_title("Trick Success vs. Failure")
    ax.set_xticklabels(["Success", "Failure"], rotation=0)
    st.pyplot(fig)
else:
    st.write("No 'success' column found in the dataset.")

skater_name = st.selectbox("Select Skater", df["skater_name"].unique())
skater_data = df[df["skater_name"] == skater_name]
st.subheader(f"Tricks by {skater_name}")
st.write(skater_data)

trick_type = st.selectbox("Select Trick Type", df["trick_name"].unique())
trick_data = df[df["trick_name"] == trick_type]
st.subheader(f"Details for {trick_type}")
st.write(trick_data)

st.success("Dashboard Ready!")
