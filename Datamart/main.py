import argparse
import logging
import os
import uuid
from dotenv import load_dotenv
from logger.logging_config import setup_logging

# Load environment variables
load_dotenv()

# Generate a job_id to use as the log file name
job_id = str(uuid.uuid4())

# Conditionally import the correct modules for Collibra based on the environment
if os.getenv('ENV', 'PRODUCTION') == 'TEST':
    from Collibra.mock_data import Collibra
else:
    from Collibra.api import Collibra

# Conditionally import the correct database handler based on the environment
if os.getenv('ENV', 'PRODUCTION') == 'TEST':
    from db_handler.db_sqlite import (
        get_connection,
        create_tables,
        insert_assets,
        insert_users,
        insert_scorecard_results,
        truncate_tables
    )
else:
    from db_handler.db_gcp import (
        get_connection,
        create_tables,
        insert_assets,
        insert_users,
        insert_scorecard_results,
        truncate_tables
    )

__appname__ = "Datamart"
__version__ = "0.1.0"
__description__ = "Load data from the Collibra API and Oracle into the DQ-DataMart"

def main(log_name: str = None, write_logs: bool = False, log_level: str = 'INFO'):
    """
    The main function to set up logging, fetch data, and handle database operations.

    Args:
        log_name (str, optional): The name of the log file to write to (optional).
        write_logs (bool): Flag indicating whether to write logs to a file.
        log_level (str): The logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL).
    """
    # Set up logging
    log_file_name = log_name or job_id
    setup_logging(log_file_name, write_logs)
    logging.getLogger().setLevel(log_level.upper())

    # Create an instance of Collibra (either real or mock depending on the environment)
    collibra = Collibra()

    # Fetch data from Collibra API
    logging.info("Fetching assets data from Collibra.")
    assets_data = collibra.get_assets()
    logging.info("Fetching users data from Collibra.")
    users_data = collibra.get_users()

    # Process the fetched data
    logging.info("Processing assets data.")
    # processed_assets = process_assets_data(assets_data)
    logging.info("Processing users data.")
    # processed_users = process_users_data(users_data)

    # Fetch scorecard data from Oracle
    logging.info("Fetching scorecard data from Oracle.")
    # scorecard_data = fetch_oracle_data()
    
    # Set up the target database
    connection = get_connection()

    try:
        # Create necessary tables if they don't exist
        create_tables(connection)
        
        # Truncate existing data
        logging.info("Truncating tables before inserting new data.")
        truncate_tables(connection)

        # Insert processed data into the target database
        logging.info("Inserting processed assets into the target database.")
        # insert_assets(connection, processed_assets)
        logging.info("Inserting processed users into the target database.")
        # insert_users(connection, processed_users)
        logging.info("Inserting scorecard results into the target database.")
        # insert_scorecard_results(connection, scorecard_data)

        logging.info("All data inserted successfully into the database.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument('--log_name', type=str, default=None, help="Name of the log file")
    parser.add_argument('--write_logs', action='store_true', default=False, help="Whether to write logs to a file")
    parser.add_argument('--log_level', type=str, default='INFO', help="Set the log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)")
    args = parser.parse_args()

    main(args.log_name, args.write_logs, args.log_level)
