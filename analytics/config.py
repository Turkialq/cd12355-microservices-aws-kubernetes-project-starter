import logging
import os
import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db_username = os.environ["DB_USERNAME"]
db_password = os.environ["DB_PASSWORD"]
db_host = os.environ.get("DB_HOST", "127.0.0.1")
db_port = os.environ.get("DB_PORT", "5432")
db_name = os.environ.get("DB_NAME", "postgres")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

db = SQLAlchemy(app)

app.logger.setLevel(logging.DEBUG)

def seed_database():
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_username,
        password=db_password,
        host=db_host,
        port=db_port
    )
    cursor = conn.cursor()
    
    # Check if both the 'users' and 'tokens' tables exist
    cursor.execute("SELECT to_regclass('public.users')")
    users_table_exists = cursor.fetchone()[0] is not None

    cursor.execute("SELECT to_regclass('public.tokens')")
    tokens_table_exists = cursor.fetchone()[0] is not None

    if not users_table_exists or not tokens_table_exists:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        db_folder = os.path.join(current_directory, 'db')
        seed_files = ['1_create_tables.sql', '2_seed_users.sql', '3_seed_tokens.sql']  
        for seed_file in seed_files:
            file_path = os.path.join(db_folder, seed_file)
            with open(file_path, 'r') as f:
                cursor.execute(f.read())
        conn.commit()

    cursor.close()
    conn.close()

@app.before_request
def initialize_database():
    seed_database()
