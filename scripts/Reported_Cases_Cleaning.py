import pandas as pd

# Load Dataset 
print("Loading Data......")

df = pd.read_excel("../data/raw/reported-cases-data.xlsx")

print("Data Loaded Successfully.")

# Standardize column names

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Handle missing values 

## Numeric columns : fill missing cases with 0

df['cases'] = pd.to_numeric(df['cases'], errors='coerce').fillna(0).astype(int)

# Year : Fill null values with Zero(0)

df['year'] = df['year'].fillna(0).astype(int)
df['year'] = pd.to_numeric(df['year'], errors = 'coerce').astype(int)

# Categorical Columns : replace NaN with "Unknown"

for col in ['group', 'code', 'name', 'disease', 'disease_description']:
    df[col] = df[col].fillna("Unknown").astype(str).str.strip()


# Remove Duplicates

df.drop_duplicates(inplace = True)

# Ensure Consistency 

df['code'] = df['code'].str.upper()
df['name'] = df['name'].str.title()
df['disease'] = df['disease'].str.upper()
df['disease_description'] = df['disease_description'].str.strip().str.title()

# Derived Features 

df['is_zero_cases'] = df['cases'].apply(lambda x : 1 if x == 0 else 0)

print("Data cleaning and preprocessing done.")

# Save Cleaned Dataset

df.to_csv("../data/processed/reported_cases_cleaned.csv", index=False)

print("Cleaned file saved as reported_cases_cleaned.csv")