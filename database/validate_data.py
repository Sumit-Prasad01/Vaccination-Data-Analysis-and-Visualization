import pandas as pd
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

# 1. Config

USER = os.getenv("USER")          
PASSWORD = os.getenv("PASSWORD") 
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DB_NAME = os.getenv("DBNAME")


DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)


# 2. Files and tables mapping

files_to_tables = {
    "../data/processed/coverage_data_cleaned.csv": "coverage_data",
    "../data/processed/incidence_rate_cleaned.csv": "incidence_rate",
    "../data/processed/reported_cases_cleaned.csv": "reported_cases",
    "../data/processed/vaccine_intro_cleaned.csv": "vaccine_intro",
    "../data/processed/vaccine_schedule_cleaned.csv": "vaccine_schedule"
}


# 3. Validation pipeline

validation_results = []

with engine.connect() as connection:
    for file, table in files_to_tables.items():
        # Count rows in CSV
        csv_rows = pd.read_csv(file).shape[0]

        # Count rows in DB table
        db_rows = connection.execute(text(f"SELECT COUNT(*) FROM {table}")).scalar()

        # Compare
        status = " MATCH" if csv_rows == db_rows else f" MISMATCH (CSV={csv_rows}, DB={db_rows})"

        validation_results.append({
            "table": table,
            "csv_rows": csv_rows,
            "db_rows": db_rows,
            "status": status
        })


# 4. Print results

print("\n Validation Results:")
for res in validation_results:
    print(f"{res['table']}: CSV={res['csv_rows']} | DB={res['db_rows']} → {res['status']}")
