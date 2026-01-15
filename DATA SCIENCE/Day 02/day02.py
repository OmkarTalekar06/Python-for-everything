import pandas as pd

data = pd.read_csv(
    "/Projects/Linked In projects/60 Days Python for everything/Data Science/Day 02/students.csv"
)

# remove rows with missing values
clean_data = data.dropna()

# double-check
print(clean_data.isnull().sum())

# save only cleaned data
clean_data.to_excel(
    "/Projects/Linked In projects/60 Days Python for everything/Data Science/Day 02/students_cleaned.xlsx",
    index=False
)

print("Clean Excel created successfully")
