import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import datetime

# Load Data
df = pd.read_csv("mentor_visit_data.csv")  # Assume the data is saved in this file

df['Date'] = pd.to_datetime(df['Date']).dt.date
df['Month'] = df['Date'].astype(str).str[:7]  # Extract year-month

# 4. Overall % for Key Metrics
metrics = ['Using Letter Trackers', 'Groups_Correct', 'Completing Admin']
metric_percentages = df[metrics].mean() * 100

st.subheader("Overall Key Metric Percentages")

figs = []
metric_labels = ["Are TA's Using Letter Trackers Correctly", "Are TA's Kids Grouped Correctly", "Are TA's Completing Admin"]
colors = [["#636EFA", "#EF553B"], ["#00CC96", "#FFA15A"], ["#AB63FA", "#FFA07A"]]

for i, metric in enumerate(metrics):
    fig = go.Figure()
    fig.add_trace(go.Pie(
        labels=["Yes", "No"],
        values=[metric_percentages[metric], 100 - metric_percentages[metric]],
        hole=0.4,
        marker=dict(colors=colors[i]),
    ))
    fig.update_layout(title_text=metric_labels[i])
    st.plotly_chart(fig)

# 1. Total Schools Visited Per Mentor
mentor_school_counts = df.groupby('Mentor Name')['School Visited'].nunique().reset_index()
st.subheader("Total Schools Visited Per Mentor")
fig = px.bar(mentor_school_counts, x='Mentor Name', y='School Visited',
             title="Total Schools Visited Per Mentor", color='School Visited',
             color_continuous_scale="Blues")
st.plotly_chart(fig)

# 2. Schools Visited Per Mentor Per Month
st.subheader("Schools Visited Per Mentor Per Month")
mentor_monthly_visits = df.groupby(['Mentor Name', 'Month'])['School Visited'].nunique().reset_index()
fig = px.line(mentor_monthly_visits, x='Month', y='School Visited', color='Mentor Name',
              title="Schools Visited Per Mentor Per Month", markers=True)
st.plotly_chart(fig)

# 4. Schools Sorted by Most Recent Quality of Sessions
st.subheader("Schools Sorted by Most Recent Quality of Sessions")
latest_quality_scores = df.groupby('School Visited').apply(lambda x: x.sort_values(by='Date', ascending=False).iloc[0])
latest_quality_scores = latest_quality_scores[['School Visited', 'Quality of Sessions']].sort_values(by='Quality of Sessions', ascending=False)
fig = px.bar(latest_quality_scores, x='School Visited', y='Quality of Sessions',
             title="Most Recent Quality of Sessions by School", color='Quality of Sessions',
             color_continuous_scale="Viridis")
st.plotly_chart(fig)

# 3. Top 5 Schools That Haven't Been Visited Recently
most_recent_visits = df.groupby(['School Visited', 'Mentor Name'])['Date'].max().reset_index()
most_recent_visits['Days Since Last Visit'] = (datetime.date.today() - most_recent_visits['Date']).apply(lambda x: x.days)
most_recent_visits = most_recent_visits.sort_values(by='Date')

st.subheader("Top 5 Schools Not Visited Recently")
st.write(most_recent_visits.head(5))

# 5. Recent Supplies Requests and Comments
st.subheader("Recent Supplies Requests")
recent_supplies = df[['School Visited', 'Supplies Needed']].tail(10)
st.write(recent_supplies)

# 6. School-specific Commentary
st.subheader("View Commentary for a Specific School")
school_selected = st.selectbox("Select a school", df['School Visited'].unique())
filtered_comments = df[df['School Visited'] == school_selected]['Commentary']
st.write(filtered_comments)
