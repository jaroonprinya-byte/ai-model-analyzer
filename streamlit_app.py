import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 AI Model Analysis Dashboard")
st.write("Upload your model results to analyze performance.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.write(df.head())

    # Example: Simple Accuracy Metric
    if 'actual' in df.columns and 'predicted' in df.columns:
        accuracy = (df['actual'] == df['predicted']).mean()
        st.metric(label="Model Accuracy", value=f"{accuracy:.2%}")
        st.line_chart(df[['actual', 'predicted']])
