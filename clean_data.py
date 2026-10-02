import pandas as pd

#Data Cleaning
print("Begin Data Cleaning...")

df = pd.read_csv('raw_data.csv')
print("Locked and Loaded")
print (df.head(5))

df = df.drop_duplicates() #removes duplicates
df = df.fillna(0) #fills missing values with zeros
df.to_csv('cleaned_data.csv', index=False)
print("Cleaning complete")
