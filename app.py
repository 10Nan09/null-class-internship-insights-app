import pandas as pd
import streamlit as st

st.title("Job Recommendation App")

# Load cleaned dataset
try:
    df = pd.read_csv("cleaned_jobs.csv")
    st.success("Cleaned dataset loaded successfully!")
except FileNotFoundError:
    st.error("cleaned_jobs.csv not found! Please upload dataset below.")
    df = None

# Allow user upload (backup option)
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Uploaded dataset loaded successfully!")

# If data is available, show preview
if df is not None:
    st.write("Preview of dataset:")
    st.dataframe(df.head())
