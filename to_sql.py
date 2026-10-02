import pandas as pd
import sqlite3

print("Converting CSV to SQL...")
df = pd.read_csv ('cleaned_data.csv') #pd.read tells python to open the file

conn = sqlite3.connect('project_database.db') #opens a local file with project_database as the name

df.to_sql('sales_table', conn, if_exists='replace', index=False) #Shovels data into SQL file
conn.close()

print("Complete. 'project_database.db' is ready for querying.")

