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



# File uploaders
st.subheader("Upload CSV Files")
full_time_file = st.file_uploader("Choose the Full-time CSV file", type="csv", key="full_time")
part_time_file = st.file_uploader("Choose the Part-time CSV file", type="csv", key="part_time")

if full_time_file is not None and part_time_file is not None:
    # Read the CSV files
    df_full_time = pd.read_csv(full_time_file)
    df_part_time = pd.read_csv(part_time_file)
    
    # Calculate the average weekly wage over all years for full-time employees
    average_full_time_wage = df_full_time.groupby('Type of work')['VALUE'].mean()
    
    # Calculate the average weekly wage over all years for part-time employees
    average_part_time_wage = df_part_time.groupby('Type of work')['VALUE'].mean()
    
    # Combine the data into a single DataFrame for easier plotting
    wages = pd.DataFrame({
        'Full-time': average_full_time_wage,
        'Part-time': average_part_time_wage
    }).reset_index()
    
    # Create a bar chart to compare the average weekly wages
    fig, ax = plt.subplots(figsize=(10, 6))
    
    x = range(len(wages['Type of work']))
    width = 0.35
    
    ax.bar([i - width/2 for i in x], wages['Full-time'], width, label='Full-time', color='blue', alpha=0.6)
    ax.bar([i + width/2 for i in x], wages['Part-time'], width, label='Part-time', color='orange', alpha=0.6)
    
    ax.set_xlabel('Type of Work')
    ax.set_ylabel('Average Weekly Wage (CAD)')
    ax.set_title('Comparison of Average Weekly Wages: Full-time vs Part-time')
    ax.set_xticks(x)
    ax.set_xticklabels(wages['Type of work'], rotation=45, ha='right')
    
    # Move legend to upper right corner
    ax.legend(loc='upper right')
    
    # Adjust layout to prevent cutting off labels
    plt.tight_layout()
    
    # Display the plot in Streamlit
    st.pyplot(fig)
   
    # Display the data
    st.subheader("Wage Data")
    st.write(wages)
    
    # Calculate and display the wage difference
    st.subheader("Wage Difference Analysis")
    wages['Difference'] = wages['Full-time'] - wages['Part-time']
    wages['Percentage Difference'] = (wages['Difference'] / wages['Part-time']) * 100
    
    st.write("Absolute difference in wages (Full-time - Part-time):")
    st.write(wages[['Type of work', 'Difference']])
    
    st.write("Percentage difference in wages:")
    st.write(wages[['Type of work', 'Percentage Difference']])
    
    # Provide some insights
    st.subheader("Insights")
    avg_diff = wages['Difference'].mean()
    avg_percent_diff = wages['Percentage Difference'].mean()
    
    st.write(f"On average, full-time employees earn ${avg_diff:.2f} more per week than part-time employees.")
    st.write(f"This represents an average {avg_percent_diff:.2f}% higher wage for full-time employees.")
    
    if avg_diff > 0:
        st.write("Based on this data, it appears to be financially advantageous to be a full-time employee rather than a part-time employee.")
    else:
        st.write("Interestingly, based on this data, part-time employees seem to earn more on average than full-time employees. This is unusual and might warrant further investigation.")

else:
    st.write("Please upload both CSV files to visualize the data.")
