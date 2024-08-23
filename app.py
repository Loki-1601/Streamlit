import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Streamlit title and description
#st.title("Hourly Wage Trends in Canada Over Time by Occupation")

#Load multiple files needed for analysis
#uploaded_files = st.file_uploader(
   # "Choose a CSV file", accept_multiple_files=True
#)
#for uploaded_file in uploaded_files:
    #bytes_data = uploaded_file.read()
    #st.write("filename:", uploaded_file.name)
    #st.write(bytes_data)
# Streamlit app title and description
st.title("Hourly Wage Trends in Canada Over Time by Occupation")
st.write("This app visualizes the average hourly wage trends for different occupations in Canada.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file, sep='\t')
    
    # Filter the DataFrame for the selected occupations
    selected_occupations = [
        'Professional occupations in engineering [213]',
        'Professional occupations in health [31]',
        'Total employees, all occupations [00-95]'
    ]
    filtered_df = df[df['National Occupational Classification (NOC)'].isin(selected_occupations)]
    
    # Create the line plot
    fig, ax = plt.subplots(figsize=(12, 6))
    
    for occupation in filtered_df['National Occupational Classification (NOC)'].unique():
        subset = filtered_df[filtered_df['National Occupational Classification (NOC)'] == occupation]
        ax.plot(subset['REF_DATE'], subset['VALUE'], label=occupation)
    
    ax.set_xlabel('Year')
    ax.set_ylabel('Average Hourly Wage (CAD)')
    ax.set_title('Hourly Wage Trends Over Time by Occupation')
    ax.legend(title='Occupation', loc='upper left', bbox_to_anchor=(1, 1))
    ax.grid(True)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Adjust layout to prevent cutting off labels
    plt.tight_layout()
    
    # Display the plot in Streamlit
    st.pyplot(fig)
    
    # Allow users to view the raw data
    if st.checkbox("Show raw data"):
        st.write(filtered_df)
else:
    st.write("Please upload a CSV file to visualize the data.")
