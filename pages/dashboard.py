import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("mentor_visit_data.csv")  # Assume the data is saved in this file

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%Y-%m')  # Extract year-month

# 4. Overall % for Key Metrics
metrics = ['Using Letter Trackers', 'Groups_Correct', 'Completing Admin']
metric_percentages = df[metrics].mean() * 100

st.subheader("Overall Key Metric Percentages")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
metric_labels = ["Using Letter Trackers", "Groups Correct", "Completing Admin"]

for i, metric in enumerate(metrics):
    values = [metric_percentages[metric], 100 - metric_percentages[metric]]
    axes[i].pie(values, labels=["Yes", "No"], autopct='%1.1f%%', startangle=90)
    axes[i].set_title(metric_labels[i])

st.pyplot(fig)

# 1. Total Schools Visited Per Mentor
mentor_school_counts = df.groupby('Mentor Name')['School Visited'].nunique()
st.subheader("Total Schools Visited Per Mentor")
st.bar_chart(mentor_school_counts)

# 2. Schools Visited Per Mentor Per Month
st.subheader("Schools Visited Per Mentor Per Month")
mentor_monthly_visits = df.groupby(['Mentor Name', 'Month'])['School Visited'].nunique().unstack()
st.line_chart(mentor_monthly_visits.T)

# 3. Top 5 Schools That Haven't Been Visited Recently
most_recent_visits = df.groupby('School Visited')['Date'].max().sort_values()
st.subheader("Top 5 Schools Not Visited Recently")
st.write(most_recent_visits.head(5))



# 5. Recent Supplies Requests and Comments
st.subheader("Recent Supplies Requests")
recent_supplies = df[['School Visited', 'Supplies Needed', 'Commentary']].tail(10)
st.write(recent_supplies)

# 6. School-specific Commentary
st.subheader("View Commentary for a Specific School")
school_selected = st.selectbox("Select a school", df['School Visited'].unique())
filtered_comments = df[df['School Visited'] == school_selected]['Commentary']
st.write(filtered_comments)
