class Collibra:
    """
    A mock version of the Collibra API class, returning predefined data.
    """

    def get_assets(self, params=None):
        return {
            "total": 1000,
            "offset": 10,
            "limit": 100,
            "results": [
                {
                    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
                    "createdBy": "4d250cc5-e583-4640-9874-b93d82c7a6cb",
                    "createdOn": 1475503010320,
                    "lastModifiedBy": "a073ff90-e7bc-4b35-ba90-c4d475f642fe",
                    "lastModifiedOn": 1476703764163,
                    "system": True,
                    "resourceType": "View",
                    "name": "Test name",
                    "displayName": "string",
                    "articulationScore": 89.5,
                    "excludedFromAutoHyperlinking": True,
                    "domain": {
                        "id": "2b7f3a1a-4e50-4077-96f0-a58a395c860d",
                        "resourceType": "Community",
                        "name": "string"
                    },
                    "type": {
                        "id": "2b7f3a1a-4e50-4077-96f0-a58a395c860d",
                        "resourceType": "Community",
                        "name": "string"
                    },
                    "status": {
                        "id": "2b7f3a1a-4e50-4077-96f0-a58a395c860d",
                        "resourceType": "Community",
                        "name": "string"
                    },
                    "avgRating": 0,
                    "ratingsCount": 0
                }
            ]
        }

    def get_users(self, params=None):
        return {
            "total": 1000,
            "offset": 10,
            "limit": 100,
            "results": [
                {
                    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
                    "userName": "johndoe",
                    "firstName": "John",
                    "lastName": "Doe",
                    "emailAddress": "johndoe@example.com",
                    "gender": "MALE",
                    "language": "English"
                }
            ]
        }

    def post_some_data(self, endpoint, data=None):
        """
        Mock POST request handling.

        Args:
            endpoint (str): The mock API endpoint.
            data (dict, optional): The data to simulate sending in the POST request.

        Returns:
            dict: Mock response for the POST request.
        """
        return {"status": "success", "message": f"Data posted to {endpoint}"}
