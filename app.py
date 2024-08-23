import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Comprehensive Wage Analysis Dashboard")
st.write("This app performs various analyses on wage data across different employment types and occupations.")

# File uploaders
st.sidebar.header("Upload Data Files")
overall_file = st.sidebar.file_uploader("Upload Overall Hourly Wages CSV", type="csv", key="overall")
fulltime_file = st.sidebar.file_uploader("Upload Full-time Weekly Wages CSV", type="csv", key="fulltime")
parttime_file = st.sidebar.file_uploader("Upload Part-time Weekly Wages CSV", type="csv", key="parttime")

# Function to load and process data
@st.cache_data
def load_data(file, sep='\t'):
    return pd.read_csv(file, sep=sep)

# Check if all files are uploaded
if overall_file and fulltime_file and parttime_file:
    # Load datasets
    df_overall = load_data(overall_file)
    df_fulltime = load_data(fulltime_file, sep=',')
    df_parttime = load_data(parttime_file, sep=',')

    # Analysis 1: Hourly Wage Trends Over Time by Occupation
    st.header("1. Hourly Wage Trends Over Time by Occupation")
    
    # Select occupations for comparison
    selected_occupations = [
        'Professional occupations in engineering [213]',
        'Professional occupations in health [31]',
        'Total employees, all occupations [00-95]'
    ]
    
    # Filter the DataFrame for the selected occupations
    trend_df = df_overall[df_overall['National Occupational Classification (NOC)'].isin(selected_occupations)]
    
    # Create the line plot
    fig, ax = plt.subplots(figsize=(12, 6))
    for occupation in trend_df['National Occupational Classification (NOC)'].unique():
        subset = trend_df[trend_df['National Occupational Classification (NOC)'] == occupation]
        ax.plot(subset['REF_DATE'], subset['VALUE'], label=occupation)
    
    ax.set_xlabel('Year')
    ax.set_ylabel('Average Hourly Wage (CAD)')
    ax.set_title('Hourly Wage Trends Over Time by Occupation')
    ax.legend(title='Occupation', loc='upper left', bbox_to_anchor=(1, 1))
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

    # Analysis 2: Full-time vs Part-time Wage Comparison
    st.header("2. Full-time vs Part-time Wage Comparison")
    
    # Calculate average wages
    avg_fulltime = df_fulltime.groupby('Type of work')['VALUE'].mean()
    avg_parttime = df_parttime.groupby('Type of work')['VALUE'].mean()
    
    # Combine data
    wages = pd.DataFrame({
        'Full-time': avg_fulltime,
        'Part-time': avg_parttime
    }).reset_index()

    # Create bar plot
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
    ax.legend(loc='upper right')
    plt.tight_layout()
    st.pyplot(fig)

    # Analysis 3: Top 5 Occupations Analysis
    st.header("3. Top 5 Occupations Analysis")
    
    # Calculate top 5 occupations
    occupation_mean_wages = df_overall.groupby('National Occupational Classification (NOC)')['VALUE'].mean()
    top_5_occupations = occupation_mean_wages.sort_values(ascending=False).head(5).index
    top_5_df = df_overall[df_overall['National Occupational Classification (NOC)'].isin(top_5_occupations)]
    
    # Create heatmap
    heatmap_data = top_5_df.pivot_table(index='National Occupational Classification (NOC)', 
                                        columns='Sex', values='VALUE', aggfunc='mean')
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    plt.title('Top 5 Occupations with Highest Average Wages by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Occupation')
    st.pyplot(fig)

    # Analysis 4: Top 3 and Bottom 3 Occupations Comparison
    st.header("4. Top 3 and Bottom 3 Occupations Comparison")
    
    # Identify bottom 3 occupations
    bottom_3_occupations = occupation_mean_wages.sort_values(ascending=True).head(3).index
    top_3_df = df_overall[df_overall['National Occupational Classification (NOC)'].isin(top_5_occupations[:3])]
    bottom_3_df = df_overall[df_overall['National Occupational Classification (NOC)'].isin(bottom_3_occupations)]
    
    # Create boxplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 16))
    
    sns.boxplot(x='National Occupational Classification (NOC)', y='VALUE', hue='Sex', data=top_3_df, ax=ax1)
    ax1.set_title('Top 3 Occupations: Average Hourly Wage by Gender')
    ax1.set_xlabel('Occupation')
    ax1.set_ylabel('Hourly Wage (CAD)')
    ax1.tick_params(axis='x', rotation=45)
    
    sns.boxplot(x='National Occupational Classification (NOC)', y='VALUE', hue='Sex', data=bottom_3_df, ax=ax2)
    ax2.set_title('Bottom 3 Occupations: Average Hourly Wage by Gender')
    ax2.set_xlabel('Occupation')
    ax2.set_ylabel('Hourly Wage (CAD)')
    ax2.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    st.pyplot(fig)

    

else:
    st.write("Please upload all three CSV files to begin the analysis.")
