import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("EDA Dashboard")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("### Data Preview")
    st.dataframe(df.head())

    st.write("### Summary Statistics")
    st.write(df.describe())

    st.write("### Missing Values")
    st.write(df.isnull().sum())

    # Plot numerical column
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    if len(numeric_cols) > 0:
        col = st.selectbox("Select a numeric column", numeric_cols)
        fig, ax = plt.subplots()
        df[col].hist(ax=ax, bins=20)
        st.pyplot(fig)
