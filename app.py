import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit title and description
st.title("Hourly Wage Trends in Canada Over Time by Occupation")
st.write("""
This visualization compares the overall hourly wage trend of all occupations with those of engineering and health professionals in Canada.
""")

# Load the data
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
