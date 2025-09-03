import pandas as pd

# Load Dataset 

print("Loading Data.......")
df = pd.read_excel("../data/raw/vaccine-introduction-data.xlsx")
print("Data Loaded Successfully.")

print("Processing Data.......")

# Standardize Colimn names

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Handle Missing Values 

# Year : Fill null values with Zero(0)

df['year'] = df['year'].fillna(0).astype(int)
df['year'] = pd.to_numeric(df['year'], errors = 'coerce').astype(int)

# Text columns : fill NaN with "Unknown"

for col in ['iso_3_code', 'countryname', 'who_region', 'description', 'intro']:
    df[col] = df[col].fillna("Unknown").astype(str).str.strip()

# Remove Duplicates 

df = df.drop_duplicates()

# Ensure Consistency 

df['iso_3_code'] = df['iso_3_code'].str.upper()
df['countryname'] = df['countryname'].str.title()
df['who_region'] = df['who_region'].str.upper()

# Standardize INTRO column (Yes/No) only

df['intro'] = df['intro'].str.strip().str.lower().map({
    'yes' : "Yes", 'y' : 'Yes',
    'no' : 'No', 'n' : 'No'
}).fillna("Unknown")


# Derived Features 

# Create flag for intro 

df['intro_flag'] = df['intro'].apply(lambda x : 1 if x == "Yes" else 0)

print("Data cleaning and processing data.")

# Save cleaned dataset 

df.to_csv("../data/processed/vaccine_intro_cleaned.csv", index = False)

print("Cleaned file saved as vaccine_intro_cleaned.csv")