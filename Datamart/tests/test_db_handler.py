import unittest
import sqlite3
import os
from db_handler.db_sqlite import (
    create_tables,
    insert_assets,
    insert_users,
    truncate_tables,
    retrieve_sample_records,
    get_connection,
    recreate_database
)

class TestDatabaseHandler(unittest.TestCase):
    def setUp(self):
        """
        Set up the database for testing.
        """
        self.connection = get_connection(':memory:')
        create_tables(self.connection)

    def tearDown(self):
        """
        Close the database connection after each test.
        """
        self.connection.close()

    def test_create_tables(self):
        """
        Test that tables are created successfully.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        self.assertIn(('Assets',), tables)
        self.assertIn(('Users',), tables)

    def test_insert_and_retrieve_assets(self):
        """
        Test inserting and retrieving assets from the database.
        """
        assets_data = [
            ("1", "Asset1", "Active", "user1", "2023-01-01 00:00:00", "user2", "2023-01-02 00:00:00"),
            ("2", "Asset2", "Inactive", "user3", "2023-02-01 00:00:00", "user4", "2023-02-02 00:00:00")
        ]
        insert_assets(self.connection, assets_data)

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Assets;")
        assets = cursor.fetchall()
        self.assertEqual(len(assets), 2)
        self.assertEqual(assets[0][1], "Asset1")

    def test_truncate_tables(self):
        """
        Test truncating tables in the database.
        """
        assets_data = [
            ("1", "Asset1", "Active", "user1", "2023-01-01 00:00:00", "user2", "2023-01-02 00:00:00")
        ]
        insert_assets(self.connection, assets_data)
        truncate_tables(self.connection)

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Assets;")
        assets = cursor.fetchall()
        self.assertEqual(len(assets), 0)

    def test_recreate_database(self):
        """
        Test recreating the database.
        """
        recreate_database(self.connection)

        cursor = self.connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        self.assertIn(('Assets',), tables)
        self.assertIn(('Users',), tables)

if __name__ == '__main__':
    unittest.main()
