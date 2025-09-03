import sqlalchemy
from sqlalchemy import create_engine, text
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# 1. Config

USER = os.getenv("USER")          
PASSWORD = os.getenv("PASSWORD") 
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DB_NAME = os.getenv("DBNAME")
SCHEMA_PATH = os.getenv("SCHEMA_PATH")

# 2. Create database (using psycopg2 because SQLAlchemy cannot create DB directly)

conn = psycopg2.connect(
    dbname="postgres",
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT
)
conn.autocommit = True
cur = conn.cursor()

# Drop and recreate the database
cur.execute(f"DROP DATABASE IF EXISTS {DB_NAME}")
cur.execute(f"CREATE DATABASE {DB_NAME}")
print(f"Database '{DB_NAME}' created successfully!")

cur.close()
conn.close()


# 3. Connect to vaccination_db using SQLAlchemy

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    
    # 4. Load schema from external file
    
    with open(SCHEMA_PATH, "r") as f:
        schema_sql = f.read()
    
    # Execute schema (can contain multiple CREATE TABLE statements)
    for statement in schema_sql.split(";"):
        if statement.strip():  # avoid empty statements
            connection.execute(text(statement))
    
    print(" All tables created successfully from schema.sql!")
