import unittest
from db_oracle import fetch_oracle_data, get_mock_data

class TestDBOracle(unittest.TestCase):

    def test_fetch_oracle_data(self):
        """
        Test fetching Oracle data (mocked for testing).
        """
        data = fetch_oracle_data()
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0][0], 'Tool A')

    def test_get_mock_data(self):
        """
        Test getting mock data.
        """
        data = get_mock_data()
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0][0], 'Tool A')

if __name__ == '__main__':
    unittest.main()
