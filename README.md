# SolarRadiationDataAnalysis

Task 1:
Git and GitHub
Tasks: 
Setting up Python environment
Git version control 
CI/CD 
Key Performance Indicators (KPIs):
Dev Environment Setup.
Relevant skill in the area demonstrated.
Suggested folder structure:
├── .vscode/

│   └── settings.json

├── .github/

│   └── workflows

│       ├── unittests.yml

├── .gitignore

├── requirements.txt

├── README.md

 |------ src/

├── notebooks/

│   ├── __init__.py

│   └── README.md

├── tests/

│   ├── __init__.py

└── scripts/

    ├── __init__.py

    └── README.md

Project Planning - EDA & Stats
Tasks: 
Data Understanding
Exploratory Data Analysis (EDA)
Statistical thinking
KPIs:
Proactivity to self-learn - sharing references.
EDA techniques to understand data and discover insights,
Demonstrating Stats understanding by using suitable statistical distributions and plots to provide evidence for actionable insights gained from EDA.
Minimum Essential To Do

Create a github repository that you will be using to host all the code for this week.
Create at least one new branch called ”task-1” for your analysis of day 1
Commit your work at least three times a day with a descriptive commit message
Perform Exploratory Data Analysis (EDA) analysis on the following:
Summary Statistics: Calculate the mean, median, standard deviation, and other statistical measures for each numeric column to understand data distribution.
Data Quality Check: Look for missing values, outliers, or incorrect entries (e.g., negative values where only positive should exist), especially in columns like GHI, DNI, and DHI.
Time Series Analysis: Analyze how variables like GHI, DNI, DHI, and Tamb change over time. You can plot these metrics across the 'Timestamp' to identify patterns or anomalies.
Correlation Analysis: Determine the correlation between different variables like solar radiation components (GHI, DHI, DNI) and temperature measures (TModA, TModB) to uncover relationships.
Wind Analysis: Explore wind speed (WS, WSgust, WSstdev) and wind direction (WD, WDstdev) data to identify any trends or notable wind events.
Temperature Analysis: Compare module temperatures (TModA, TModB) with ambient temperature (Tamb) to see how they are related or vary under different conditions.
Histograms: Create histograms for variables like GHI, DNI, DHI, WS, and temperatures to visualize the frequency distribution of these variables.
Box Plots: Use box plots to examine the spread and presence of outliers in the solar radiation and temperature data.
Scatter Plots: Generate scatter plots to explore the relationships between pairs of variables, such as GHI vs. Tamb, WS vs. WSgust, or any other potentially interesting pairs.
Data Cleaning: Based on the initial analysis, clean the dataset by handling anomalies and missing values, especially in columns like Comments which appear entirely null.
Task 2:
Dashboard Development Using Streamlit
Tasks:
Designing and developing a dashboard using Streamlit to visualize data insights.
Integrating Python scripts to fetch and process data dynamically.
Implementing interactive features (e.g., sliders, buttons) to allow users to customize visualizations.
Deploying the Streamlit dashboard to Streamlit Community Cloud. 
KPIs
Dashboard Usability: Ease of use, with intuitive navigation and clear labels.
Interactive Elements: Effective use of Streamlit widgets to enhance user engagement.
Visual Appeal: Clean and professional design that effectively communicates data insights.
Deployment Success: Fully functional deployment, accessible via a public URL.
Suggested Folder Structure:
├── .streamlit

│   └── config.toml

├── .vscode

│   └── settings.json

├── .github

│   └── workflows

│       ├── unittests.yml

├── .gitignore

├── requirements.txt

├── README.md

├── notebooks

│   ├── __init__.py

│   └── README.md

├── tests

│   ├── __init__.py

├── app

│   ├── __init__.py

│   ├── main.py  # main Streamlit application script

│   ├── utils.py  # utility functions for data processing and visualization

└── scripts

    ├── __init__.py

    └── README.md

Minimum Essential To Do:

Merge the necessary branches from task-1 into the main branch using a Pull Request (PR)
Create at least one new branch called "dashboard-dev" for the ongoing development of the dashboard.
Commit your work with a descriptive commit message.
Design and develop the Streamlit dashboard to visualize the dataset with interactive elements
Document the development process and usage instructions in the README.md file.
