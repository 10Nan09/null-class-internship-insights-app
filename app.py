import pandas as pd
import streamlit as st
import datetime
import altair as alt

# Load your data
df = pd.read_csv(r"C:\Users\nandh\Downloads\job_descriptions.csv")

# --- Apply Filters ---
filtered_df = df[
    (df['Work Type'] == 'Intern') &
    (df['latitude'] < 10) &
    (~df['Country'].str.startswith(tuple('ABCD'))) &
    (df['Job Title'].str.len() <= 25) &   # increased from 10 to 25
    (df['Company Size'] < 50000)
]

# --- Time-Based Display (IST) ---
current_time_utc = datetime.datetime.utcnow()
current_time_ist = current_time_utc + datetime.timedelta(hours=5, minutes=30)

if 15 <= current_time_ist.hour < 17:   # 15 = 3PM, 17 = 5PM
    st.title("Preference vs Work Type (Interns Only)")

    chart_data = filtered_df.groupby(['Preference', 'Work Type']).size().reset_index(name='count')

    st.bar_chart(
        data=chart_data,
        x='Preference',
        y='count'
    )
else:
    st.warning("⏰ This chart is only visible between 3 PM and 5 PM IST.")

# Save filtered data
filtered_df.to_csv("cleaned_jobs.csv", index=False)
