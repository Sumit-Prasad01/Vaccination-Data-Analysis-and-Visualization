import pandas as pd

# Load Dataset 
print("Loading Data.......")
df = pd.read_excel("../data/raw/vaccine-schedule-data.xlsx")
print("Data Loaded Successfully.")

# Standardize Column names

df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")

# Handle Missing Values 

# Year : Fill null values with Zero(0)

df['year'] = df['year'].fillna(0).astype(int)
df['year'] = pd.to_numeric(df['year'], errors = 'coerce').astype(int)

# Numeric-like columns (schedule may be mixed : numeric + text)

df['schedulerounds'] = df['schedulerounds'].astype(str).str.strip()

# Fill NaN in categorical columns with "Unknown"

for col in ['iso_3_code', 'countryname', 'who_region', 'vaccinecode',
            'vaccine_description', 'targetpop', 'targetpop_description',
            'geoarea', 'ageadministered', 'sourcecomment']:
    df[col] = df[col].fillna("Unknown").astype(str).str.strip()

# Remove Duplicates 

df.drop_duplicates(inplace = True)

# Ensure Consistency 

df['iso_3_code'] = df['iso_3_code'].str.upper()
df['countryname'] = df['countryname'].str.title()
df['who_region'] = df['who_region'].str.upper()
df['vaccinecode'] = df['vaccinecode'].str.upper()

# Standardize geoareas

df['geoarea'] = df['geoarea'].str.title()

# Derived features 

# Create a flag for risk groups 

df['is_risk_group'] = df['targetpop'].apply(lambda x : 1 if 'RISK' in x.upper() else 0)

# Create numeric schedule if possible 

df['schedule_num'] = pd.to_numeric(df['schedulerounds'], errors='coerce')

print("Data cleaning and processing data.")

# Save Cleaned dataset

df.to_csv("../data/processed/vaccine_schedule_cleaned.csv", index=False)

print("Cleaned file saved as vaccine_schedule_cleaned.csv")