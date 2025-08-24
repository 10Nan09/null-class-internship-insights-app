import pandas as pd
import streamlit as st
import datetime

# --- Load Data ---
df = pd.read_csv("job_descriptions.csv")   # keep file in same folder or use relative path

# --- Apply Filters ---
filtered_df = df[
    (df['Work Type'] == 'Intern') &
    (df['latitude'] < 10) &
    (~df['Country'].astype(str).str.startswith(tuple('ABCD'))) &  # ensure string type
    (df['Job Title'].astype(str).str.len() <= 25) &
    (df['Company Size'] < 50000)
]

# --- Time-Based Display (IST) ---
current_time_utc = datetime.datetime.utcnow()
current_time_ist = current_time_utc + datetime.timedelta(hours=5, minutes=30)

if 15 <= current_time_ist.hour < 17:   # 3PM–5PM IST
    st.title("Preference vs Work Type (Interns Only)")

    chart_data = filtered_df.groupby(['Preference', 'Work Type']).size().reset_index(name='count')

    st.bar_chart(chart_data.set_index('Preference')['count'])
else:
    st.warning("⏰ This chart is only visible between 3 PM and 5 PM IST.")

# --- Save Filtered Data ---
filtered_df.to_csv("cleaned_jobs.csv", index=False)
