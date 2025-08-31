import pandas as pd

# Load Dataset
print("Loading data.......")

df = pd.read_excel("../data/raw/coverage-data.xlsx")

print("Data loaded successfully.")
# Standardize column names

print("Processing Data...")

df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")

# Handle Missing Values
## Fill missing numeric values with 0 (TARGET_NUMBER, DOSES, COVERAGE)

df['target_number'] = df['target_number'].fillna(0).astype(int)
df['doses'] = df['doses'].fillna(0).astype(int)
df['coverage'] = df['coverage'].fillna(0).astype(int)

# Fill missing categorical values with "unknown"

for col in ['group', 'code', 'name', 'antigen', 'antigen_description', 
            'coverage_category', 'coverage_category_description']:
    
    df[col] = df[col].fillna('Unknown')


# Remove Duplicates

df.drop_duplicates(inplace = True)

# Ensure Consistency
df['year'] = df['year'].fillna(0).astype(int)
df['year'] = df['year'].astype(int)

# Standardize text columns (trim + uppercase codes, title case names)

df['code'] = df['code'].str.strip().str.upper()
df['name'] = df['name'].str.strip().str.title()
df['antigen'] = df['antigen'].str.strip().str.upper()

# Create Divide features 

# Drop-off rate = (Target - Doses) / Target
df['drop_off_rate'] = df.apply(
    lambda row : (row['target_number'] - row['doses']) / row['target_number']
    if row['target_number'] > 0 else 0, axis = 1
)

# Dose coverage ration = Doses / Target

df['does_coverage_ratio'] = df.apply(
    lambda row : row['doses'] / row['target_number']
    if row['target_number'] > 0 else 0, axis = 1
)

print("Data processing and cleaning completed.")
# save the cleaned dataset

print("Saving Cleaned data to a csv file.")

df.to_csv("../data/processed/coverage_data_cleaned.csv", index = False)

print("Cleaned file saved as vaccination_data_cleaned.csv")