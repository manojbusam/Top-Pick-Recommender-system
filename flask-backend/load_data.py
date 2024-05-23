import psycopg2
from sqlalchemy import create_engine
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('relevancy-toppicks.csv')

# Set max_columns option to None to display all columns
pd.set_option('display.max_columns', None)

# Display the top 10 rows
print(df.head(10))

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="recommendations_db",
    user="user",
    password="password",
    host="127.0.0.1",
    port="5432"
)

# Create SQLAlchemy engine
engine = create_engine('postgresql://', creator=lambda: conn)

# Write DataFrame to PostgreSQL
df.to_sql('toppicks_recommendations', engine, if_exists='replace', index=False)

# Confirm data has been added by querying the table
df_from_db = pd.read_sql_query('SELECT * FROM toppicks_recommendations', engine)
print(df_from_db)
