import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Streamlit title and description
st.title("Hourly Wage Trends in Canada Over Time by Occupation")

# Load the data
#uploaded_file = st.file_uploader("Choose a file")
#if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    #dataframe = pd.read_csv(uploaded_file)
    #st.write(dataframe)


uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
