import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import fetch_data, process_data, visual_data
import os

def visualize_data(df):
    """
    Visualize data including line charts, summary statistics, correlation analysis, and histograms.
    
    Args:
    df (pandas.DataFrame): Processed DataFrame.
    """
    # Add section headers
    st.header('Data Visualization')

    # Add interactive elements
    selected_variable = st.selectbox('Select Variable', ['GHI', 'DNI', 'DHI'])

    # Generate visualization based on selected variable
    if selected_variable == 'GHI':
        st.line_chart(df['GHI'])
    elif selected_variable == 'DNI':
        st.line_chart(df['DNI'])
    elif selected_variable == 'DHI':
        st.line_chart(df['DHI'])

    # Add section headers
    st.header('Summary Statistics')

    # Display summary statistics
    st.write(df.describe())

    # Add section headers
    st.header('Correlation Analysis')

    # Calculate correlation matrix
    correlation_matrix = df.corr()

    # Create a new figure and axis using plt.subplots()
    fig, ax = plt.subplots(figsize=(10, 8))

    # Display correlation matrix as heatmap on the axis
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)

    # Pass the figure object to st.pyplot()
    st.pyplot(fig)

    # Add section headers
    st.header('Histograms')

    # Display histograms for selected variables
    st.bar_chart(df[selected_variable].value_counts())

def main():
    # Add a title to the app
    st.title('Solar Data Analysis')

    # Add a sidebar with a title and description
    st.sidebar.title('Pages')
    selected_page = st.sidebar.selectbox('Select Page', ['Page 1', 'Page 2', 'Page 3'])

    # Get the current directory of the script
    current_dir = os.path.dirname(__file__)

    # Navigate to the data folder from the script folder
    data_folder = os.path.join(current_dir, '../data')

    # Load different files based on the selected page
    if selected_page == 'Page 1':
        file_name = 'benin-malanville.csv'
    elif selected_page == 'Page 2':
        file_name = 'sierraleone-bumbuna.csv'
    elif selected_page == 'Page 3':
        file_name = 'togo-dapaong_qc.csv'

    # Fetch data
    data = fetch_data(os.path.join(data_folder, file_name))

    # Process data
    try:
        processed_data = process_data(data)
        visual_data(processed_data)
        visualize_data(processed_data)
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
