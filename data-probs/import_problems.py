import csv
from sqlalchemy.orm import Session
from competition.models.task import Task, Base
from config.db import engine, SessionLocal
import sqlite3


def load_tasks_from_csv(csv_file: str, db_file: str):
    # Connect to the SQLite database (or your chosen database)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Ensure the tasks table exists
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        link TEXT,
        difficulty TEXT)
    ''')

    try:
        # Open the CSV file
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Prepare the SQL insert statement
                cursor.execute('''
                INSERT INTO tasks (title, link, difficulty)
                VALUES (?, ?, ?)
                ''', (
                    # row['id'],
                    row['title'],
                    row['url'],
                    row['difficulty']
                ))
            conn.commit()  # Commit all changes to the database
    except Exception as e:
        conn.rollback()  # Rollback in case of an error
        print(f"An error occurred: {e}")
    finally:
        conn.close()  # Close the database connection

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Import tasks from a CSV file into the database")
    parser.add_argument('csv_file', type=str, help="The path to the CSV file to be imported")
    parser.add_argument('db_file', type=str, help="The path to the SQLite database file")
    args = parser.parse_args()

    load_tasks_from_csv(args.csv_file, args.db_file)