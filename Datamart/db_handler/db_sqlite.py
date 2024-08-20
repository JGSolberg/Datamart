import sqlite3
import os
import logging

def get_connection(db_path=None):
    """
    Establish a connection to the SQLite database.

    Args:
        db_path (str): Path to the SQLite database file. Default is 'Datamart/_data/datamart.db'.

    Returns:
        sqlite3.Connection: Connection object for the SQLite database.
    """
    if db_path is None:
        db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '_data', 'datamart.db')
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    logging.info(f"Connecting to SQLite database at {db_path}.")
    return sqlite3.connect(db_path)

def create_tables(connection):
    """
    Create tables in the SQLite database.

    Args:
        connection (sqlite3.Connection): SQLite database connection object.
    """
    logging.info("Creating tables in the database.")
    with connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS Assets (
            id TEXT PRIMARY KEY,
            name TEXT,
            status TEXT,
            created_by TEXT,
            created_at TEXT,
            updated_by TEXT,
            updated_at TEXT
        )''')
        connection.execute('''CREATE TABLE IF NOT EXISTS Users (
            id TEXT PRIMARY KEY,
            userName TEXT,
            firstName TEXT,
            lastName TEXT,
            emailAddress TEXT,
            gender TEXT,
            language TEXT
        )''')
        connection.execute('''CREATE TABLE IF NOT EXISTS scorecard_results (
            Tool TEXT,
            Score_Name TEXT,
            profile_name TEXT,
            Total_rows INTEGER,
            passing_rows INTEGER,
            failing_rows INTEGER,
            passing_percent REAL,
            rundate TEXT,
            score_typ TEXT
        )''')
    logging.info("Tables created successfully.")

def drop_tables(connection):
    """
    Drop all tables in the SQLite database.

    Args:
        connection (sqlite3.Connection): SQLite database connection object.
    """
    logging.warning("Dropping all tables in the database.")
    with connection:
        connection.execute('DROP TABLE IF EXISTS Assets')
        connection.execute('DROP TABLE IF EXISTS Users')
        connection.execute('DROP TABLE IF EXISTS scorecard_results')
    logging.info("Tables dropped successfully.")

def recreate_database(connection):
    """
    Drop and recreate the database tables.

    Args:
        connection (sqlite3.Connection): SQLite database connection object.
    """
    logging.info("Recreating the database.")
    drop_tables(connection)
    create_tables(connection)
    logging.info("Database recreated successfully.")

def insert_assets(connection, assets):
    """
    Insert or replace assets data in the SQLite database.

    Args:
        connection (sqlite3.Connection): SQLite database connection object.
        assets (list of tuples): List of assets data to insert.
    """
    logging.info(f"Inserting {len(assets)} assets into the database.")
    with connection:
        try:
            connection.executemany('''
                INSERT OR REPLACE INTO Assets (id, name, status, created_by, created_at, updated_by, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', assets)
            logging.info("Assets inserted successfully.")
        except sqlite3.DatabaseError as e:
            logging.error(f"An error occurred while inserting assets: {e}")
            raise

def insert_users(connection, users):
    """
    Insert or replace users data in the SQLite database.

    Args:
        connection (sqlite3.Connection): SQLite database connection object.
        users (list of tuples): List of users data to insert.
    """
    logging.info(f"Inserting {len(users)} users into the database.")
    with connection:
        try:
            connection.executemany('''
                INSERT OR REPLACE INTO Users (id, userName, firstName, lastName, emailAddress, gender, language)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', users)
            logging.info("Users inserted successfully.")
        except sqlite3.DatabaseError as e:
            logging.error(f"An error occurred while inserting users: {e}")
            raise

def insert_scorecard_results(connection, scorecard_data):
    """
    Insert or replace scorecard results into the SQLite database.

    Args:
        connection (sqlite3.Connection): SQLite database connection object.
        scorecard_data (list of tuples): Scorecard data to insert.
    """
    logging.info(f"Inserting {len(scorecard_data)} scorecard results into the database.")
    with connection:
        try:
            connection.executemany('''
                INSERT OR REPLACE INTO scorecard_results (Tool, Score_Name, profile_name, Total_rows, passing_rows, failing_rows, passing_percent, rundate, score_typ)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', scorecard_data)
            logging.info("Scorecard results inserted successfully.")
        except sqlite3.DatabaseError as e:
            logging.error(f"An error occurred while inserting scorecard results: {e}")
            raise

def truncate_tables(connection):
    """
    Truncate all tables in the SQLite database.

    Args:
        connection (sqlite3.Connection): SQLite database connection object.
    """
    logging.warning("Truncating all tables in the database.")
    with connection:
        connection.execute('DELETE FROM Assets')
        connection.execute('DELETE FROM Users')
        connection.execute('DELETE FROM scorecard_results')
    logging.info("Tables truncated successfully.")

def retrieve_sample_records(connection, table_name, limit=5):
    """
    Retrieve and print a sample of records from the specified table.

    Args:
        connection (sqlite3.Connection): SQLite database connection object.
        table_name (str): The name of the table to retrieve records from.
        limit (int): The number of records to retrieve.
    """
    logging.info(f"Retrieving up to {limit} records from {table_name} table.")
    with connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name} LIMIT ?", (limit,))
        rows = cursor.fetchall()

        if not rows:
            print(f"No records found in {table_name} table.")
        else:
            print(f"Sample records from {table_name} table:")
            for row in rows:
                print(row)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="SQLite Database Management")
    parser.add_argument('--recreate', action='store_true', help="Drop and recreate the database tables")
    parser.add_argument('--sample', type=str, choices=['Assets', 'Users', 'scorecard_results'], help="Retrieve sample records from the specified table")
    parser.add_argument('--limit', type=int, default=5, help="Number of sample records to retrieve")
    args = parser.parse_args()

    conn = get_connection()

    if args.recreate:
        print("Recreating the database...")
        recreate_database(conn)
        print("Database recreated successfully.")

    if args.sample:
        print(f"Retrieving sample records from the {args.sample} table...")
        retrieve_sample_records(conn, args.sample, limit=args.limit)

    conn.close()
