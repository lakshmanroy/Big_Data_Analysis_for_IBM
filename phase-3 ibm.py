# Python Code

# Data Selection

import pandas as pd

# Load the dataset into a DataFrame
# rainfall_data = pd.read_csv('f'/kaggle/input/airline-delay-and-cancellation-data-2009-2018/{file}.csv'')

# Database Setup
# Assuming you have established a connection to the IBM DB2 database
import ibm_db

# Create a database instance
db2_conn = ibm_db.connect("DATABASE=BSJ92334;HOSTNAME=3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:31498;PORT=60000;PROTOCOL=TCPIP;UID=bsj92334;PWD=9xAOjpxeWtsLcMUo;", "", "")

# Data Exploration
# Assuming you want to perform a basic exploration of the dataset
# For example, checking the first few rows of data
print(rainfall_data.head())

# Analysis Techniques
# Assuming you want to perform basic statistical analysis
# For example, calculating mean and standard deviation of rainfall
mean_rainfall = rainfall_data['Rainfall'].mean()
std_dev_rainfall = rainfall_data['Rainfall'].std()
print(f"Mean Rainfall: {mean_rainfall}")
print(f"Standard Deviation of Rainfall: {std_dev_rainfall}")

# SQL Command for Creating Database Table

create_table_sql = '''
CREATE TABLE your_table_name (
    Year INT,
    Month INT,
    State VARCHAR(255),
    District VARCHAR(255),
    Rainfall FLOAT
)
'''

# Execute the SQL command to create the table
stmt = ibm_db.exec_immediate(db2_conn, create_table_sql)