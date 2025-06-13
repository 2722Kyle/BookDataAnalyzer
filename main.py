import pandas as pd

df = pd.read_csv('bestsellers.csv')

#Get the first 5 rows of the spreadsheet
print(df.head())

#Get the shape of the spreadsheet
print(df.shape)

#Get the column names of the spreadsheet
print(df.columns)

#Get the summary statistics for each column
print(df.describe())

#-----Data Cleanup-----

#Checks for and removes duplicate rows
df.drop_duplicates(inplace=True) #inplace=True changes made to original Data Frame

#Column Renaming
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

#Data type conversion to float data
df["Price"] = df["Price"].astype(float)

#-----Author Popularity Analysis-----
author_counts = df['Author'].value_counts()
print(author_counts)

#-----Average Rating by Genre-----
avg_rating = df.groupby("Genre")["Rating"].mean()
print(avg_rating)

#-----Result Exporting-----
author_counts.head(10).to_csv("Top_Authors.csv") #Exports top selling authors
avg_rating.to_csv("Average_Rating.csv") #Exports average rating by genre