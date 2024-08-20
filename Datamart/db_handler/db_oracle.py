import os
import logging

def fetch_oracle_data():
    """
    Fetch data from the Oracle view. In TEST mode, returns mock data.

    Returns:
        list of tuples: Data retrieved from the Oracle view or mock data.
    """
    if os.getenv('ENV', 'PRODUCTION') == 'TEST':
        logging.info("Environment is set to TEST. Returning mock Oracle data.")
        return get_mock_data()
    
    import cx_Oracle
    
    # Oracle connection details from environment variables
    oracle_user = os.getenv('ORACLE_USER')
    oracle_pass = os.getenv('ORACLE_PASS')
    oracle_dsn = os.getenv('ORACLE_DSN')

    logging.info(f"Connecting to Oracle database with DSN: {oracle_dsn}")
    
    try:
        connection = cx_Oracle.connect(oracle_user, oracle_pass, oracle_dsn)
        cursor = connection.cursor()
        cursor.execute("SELECT Tool, Score_Name, profile_name, Total_rows, passing_rows, failing_rows, passing_percent, rundate, score_typ FROM DQ_STG_PP.DQI_METRICS_FOR_COLLIBRA_V")
        data = cursor.fetchall()
        logging.info("Successfully fetched data from Oracle.")
        return data
    except cx_Oracle.DatabaseError as e:
        logging.error(f"Failed to fetch data from Oracle: {e}")
        raise
    finally:
        cursor.close()
        connection.close()

def get_mock_data():
    """
    Return mock data for testing purposes.

    Returns:
        list of tuples: Mock data simulating the Oracle view.
    """
    return [
        ('Tool A', 'Score 1', 'Profile 1', 1000, 950, 50, 95.0, '2024-08-20', 'Type 1'),
        ('Tool B', 'Score 2', 'Profile 2', 2000, 1900, 100, 95.0, '2024-08-20', 'Type 2'),
        ('Tool C', 'Score 3', 'Profile 3', 1500, 1450, 50, 96.7, '2024-08-20', 'Type 3'),
    ]
