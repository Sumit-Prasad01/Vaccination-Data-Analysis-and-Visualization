import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

# 1. Config

USER = os.getenv("USER")          
PASSWORD = os.getenv("PASSWORD") 
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DB_NAME = os.getenv("DBNAME")

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"


# 2. Create SQLAlchemy engine

engine = create_engine(DATABASE_URL)


# 3. Load CSVs into DataFrames

files_to_tables = {
    "../data/processed/coverage_data_cleaned.csv": "coverage_data",
    "../data/processed/incidence_rate_cleaned.csv": "incidence_rate",
    "../data/processed/reported_cases_cleaned.csv": "reported_cases",
    "../data/processed/vaccine_intro_cleaned.csv": "vaccine_intro",
    "../data/processed/vaccine_schedule_cleaned.csv": "vaccine_schedule"
}


# 4. Push data into DB

for file, table in files_to_tables.items():
    print(f" Loading {file} into {table}...")
    df = pd.read_csv(file)
    
    # Append data to table (no overwrite)
    df.to_sql(table, engine, if_exists="append", index=False)
    print(f" Loaded {len(df)} rows into {table}")

print(" All CSVs loaded into PostgreSQL successfully!")
