import os
import pandas as pd

# Get the current directory of the script
current_dir = os.path.dirname(__file__)

# Navigate to the data folder from the script folder
data_folder = os.path.join(current_dir, '../data')

# Load the data from the CSV file
df = pd.read_csv(os.path.join(data_folder, 'benin-malanville.csv'))
