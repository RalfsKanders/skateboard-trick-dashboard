import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    url = "https://raw.githubusercontent.com/RalfsKanders/skateboard-trick-dashboard/main/dataset.csv"
    df = pd.read_csv(url)
    return df

df = load_data()

st.title("Olympic Skateboarding Analytics Dashboard")
st.write("Explore skateboarding performance in the Olympic Games!")

event_type_filter = st.selectbox("Select Event Type", df['Event Type'].unique())
filtered_data = df[df['Event Type'] == event_type_filter]

st.write(f"Showing results for {event_type_filter} event")
st.dataframe(filtered_data)

st.write("Medal Type Distribution")
medal_count = df['Medal Type'].value_counts()
st.bar_chart(medal_count)

st.write("Skater Age Distribution")
st.histogram(df['Age'], bins=10, title="Age Distribution of Skaters")
st.pyplot(plt)


if 'Year' in df.columns:
    score_trends = df.groupby('Year')['Score'].mean()
    st.write("Average Score Over Time")
    st.line_chart(score_trends)


st.write("Trick Difficulty vs. Score")
plt.figure(figsize=(10,6))
plt.scatter(df['Trick Difficulty'], df['Score'], c=df['Score'], cmap='viridis')
plt.colorbar(label='Score')
plt.xlabel("Trick Difficulty")
plt.ylabel("Score")
st.pyplot(plt)

skater_name = st.text_input("Search for Skater")
if skater_name:
    skater_performance = df[df['Skater Name'].str.contains(skater_name, case=False)]
    st.write(f"Performance of {skater_name}")
    st.dataframe(skater_performance)


st.write("Raw Data")
st.dataframe(df)
