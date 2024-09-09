from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import os

load_dotenv()

# Get environment variables
TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL")
TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN")

# construct special SQLAlchemy URL
dbUrl = f"sqlite+{TURSO_DATABASE_URL}/?authToken={TURSO_AUTH_TOKEN}&secure=true"

engine = create_engine(dbUrl, connect_args={'check_same_thread': False}, echo=True)

with open('backup2.sql', 'r', encoding='utf-8-sig') as file:
    sql_script = file.read()

sql_statements = sql_script.split(';')

with engine.connect() as conn:
    for statement in sql_statements:
        statement = statement.strip()
        if statement:
            print(f"Ejecutando: {statement}")
            try:
                conn.execute(text(statement))
                conn.commit()
            except Exception as e:
                print(f"Error ejecutando la sentencia: {statement}")
                print(f"Error: {e}")

print("Datos insertados correctamente.")