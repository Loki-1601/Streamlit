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

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep='\t')

    # Filter the DataFrame for the selected occupations
    selected_occupations = df[df['National Occupational Classification (NOC)'].isin([
        'Professional occupations in engineering [213]', 
        'Professional occupations in health [31]', 
        'Total employees, all occupations [00-95]'
    ])]

    # Create the line plot
    plt.figure(figsize=(10, 6))
    for occupation in selected_occupations['National Occupational Classification (NOC)'].unique():
        subset = selected_occupations[selected_occupations['National Occupational Classification (NOC)'] == occupation]
        plt.plot(subset['REF_DATE'], subset['VALUE'], label=occupation)

    plt.xlabel('Year')
    plt.ylabel('Average Hourly Wage (CAD)')
    plt.title('Hourly Wage Trends Over Time by Occupation')
    plt.legend(title='Occupation')
    plt.grid(True)
    
    # Display the plot in Streamlit
    st.pyplot(plt)

    # Text analysis section for AI-generated insights (example text provided)
    response_message = """
    By analyzing the trends over time, it becomes evident that while the overall wage growth has been steady, certain sectors such as engineering and health professionals have shown a marked increase, reflecting the rising demand and value of these professions in the Canadian economy.
    """
    
    st.write("### Insights from the Data")
    st.write(response_message)
