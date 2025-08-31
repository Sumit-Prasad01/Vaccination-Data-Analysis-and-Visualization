import pandas as pd

# Loading  Dataset 

print("Loading Dataset.......")

df = pd.read_excel("../data/raw/incidence-rate-data.xlsx")

print("Dataset loaded successfully.")

#  Standardize column names

print("Processing and Cleaning Data")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Handle Missing Values
# Numeric cols : fill missing incidence rates with 0

df['incidence_rate'] = pd.to_numeric(df['incidence_rate'], errors = 'coerce').fillna(0)

# Year : Fill null values with Zero(0)

df['year'] = df['year'].fillna(0).astype(int)
df['year'] = pd.to_numeric(df['year'], errors = 'coerce').astype(int)

# Categorical columns : replace NaN with "Unknown"

for col in ['group', 'code', 'name', 'disease', 'disease_description', 'denominator']:
    df[col] = df[col].fillna("Unknown").astype(str).str.strip()

# Remove Duplicates

df.drop_duplicates(inplace = True)

# Ensure Consistency 

# Standardize formats 

df['code'] = df['code'].str.upper()
df['name'] = df['name'].str.title()
df['disease'] = df['disease'].str.upper()
df['disease_description'] = df['disease_description'].str.strip().str.title()

# Derived Features 

# Flag for zero incidence (useful for analysis of eradicated diseases)

df['is_zero_incidence'] = df['incidence_rate'].apply(lambda x : 1 if x == 0 else 0)

# Save cleaned dataset

print("Data Processing and Cleaning Complete.")

df.to_csv("../data/processed/incidence_rate_cleaned.csv", index = False)

print("Cleaned file saved as incidence_rate_cleaned.csv")