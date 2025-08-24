import pandas as pd
import streamlit as st

st.title("Job Recommendation App")

# ---- Load cleaned dataset ----
try:
    df = pd.read_csv("cleaned_jobs.csv")
    st.success("Cleaned dataset loaded successfully!")
except FileNotFoundError:
    st.error("cleaned_jobs.csv not found! Please upload dataset below.")
    df = None

# ---- Allow user upload (backup option) ----
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("Uploaded dataset loaded successfully!")
    except Exception as e:
        st.error(f"Error loading uploaded file: {e}")
        df = None

# ---- If data is available ----
if df is not None:
    st.write("Preview of dataset:")
    st.dataframe(df.head())
    
    # ---- Column type checks ----
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    if numeric_columns:
        st.write("Numeric columns available for chart:", numeric_columns)
        column_to_plot = st.selectbox("Select column to plot", numeric_columns)
        
        # ---- Null values check ----
        null_count = df[column_to_plot].isnull().sum()
        st.write(f"Null values in {column_to_plot}: {null_count}")
        if null_count > 0:
            st.warning(f"Dropping {null_count} null rows from column '{column_to_plot}' for chart plotting.")
            df = df.dropna(subset=[column_to_plot])
        
        # ---- Chart display ----
        st.line_chart(df[column_to_plot])
    else:
        st.warning("No numeric columns available for chart.")
else:
    st.info("Please upload a dataset to proceed.")
