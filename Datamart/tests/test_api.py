import unittest
from unittest.mock import patch
from Collibra.api import fetch_data_from_api, process_assets_data, convert_epoch_to_datetime

class TestAPI(unittest.TestCase):
    
    @patch('Collibra.api.requests.get')
    def test_fetch_data_from_api(self, mock_get):
        mock_response = {
            "total": 1,
            "results": [
                {"id": "test_id", "name": "test_name"}
            ]
        }
        mock_get.return_value.json.return_value = mock_response
        
        data = fetch_data_from_api('assets')
        
        self.assertEqual(len(data['results']), 1)
        self.assertEqual(data['results'][0]['name'], 'test_name')

    def test_convert_epoch_to_datetime(self):
        self.assertEqual(convert_epoch_to_datetime(1475503010320), '2016-10-02 15:56:50')

    def test_process_assets_data(self):
        mock_assets_data = {
            "results": [
                {
                    "id": "1",
                    "createdOn": 1475503010320,
                    "lastModifiedOn": 1476703764163,
                    "createdBy": "user1",
                    "lastModifiedBy": "user2",
                    "name": "Asset Name",
                    "status": {"name": "Active"}
                }
            ]
        }

        mock_users_data = {
            "results": [
                {"id": "user1", "userName": "John Doe"},
                {"id": "user2", "userName": "Jane Smith"}
            ]
        }

        processed_data = process_assets_data(mock_assets_data, mock_users_data)
        
        self.assertEqual(processed_data['results'][0]['createdOn'], '2016-10-02 15:56:50')
        self.assertEqual(processed_data['results'][0]['createdBy'], 'John Doe')

if __name__ == '__main__':
    unittest.main()
