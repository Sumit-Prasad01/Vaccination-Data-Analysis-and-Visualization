import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

# 1. Config

USER = os.getenv("USER")          
PASSWORD = os.getenv("PASSWORD") 
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DB_NAME = os.getenv("DBNAME")

# First connect to default database
default_engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/postgres")

with default_engine.connect() as connection:
    connection.execute(text("commit"))  # end transaction
    # Terminate sessions
    connection.execute(text(f"""
        SELECT pg_terminate_backend(pg_stat_activity.pid)
        FROM pg_stat_activity
        WHERE pg_stat_activity.datname = '{DB_NAME}'
        AND pid <> pg_backend_pid();
    """))
    # Drop + create
    connection.execute(text(f"DROP DATABASE IF EXISTS {DB_NAME}"))
    connection.execute(text(f"CREATE DATABASE {DB_NAME}"))

print(f" Database '{DB_NAME}' created successfully!")

# Now reconnect to the new DB (fresh engine)
engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}")

# Run schema
with engine.connect() as connection:
    with open("sql/schema.sql", "r") as f:
        schema_sql = f.read()
        connection.execute(text(schema_sql))

print(" Schema applied successfully!")
