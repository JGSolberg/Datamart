import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()

class Collibra:
    def __init__(self):
        self.base_url = os.getenv('COLLIBRA_URL')
        self.auth = (os.getenv('COLLIBRA_USER'), os.getenv('COLLIBRA_PASS'))
        self.proxy = {
            'http': os.getenv('PROXY'),
            'https': os.getenv('PROXY')
        }
        logging.info("Initialized Collibra API with base URL and authentication.")

    def __make_get_call(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        logging.info(f"Making GET request to {url} with params: {params}")
        try:
            response = requests.get(url, auth=self.auth, params=params, proxies=self.proxy)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"GET request failed: {e}")
            raise

    def __make_post_call(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        logging.info(f"Making POST request to {url} with data: {data}")
        try:
            response = requests.post(url, auth=self.auth, json=data, proxies=self.proxy)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"POST request failed: {e}")
            raise

    def get_assets(self, params=None):
        return self.__make_get_call('assets', params=params)

    def get_users(self, params=None):
        return self.__make_get_call('users', params=params)

    def post_some_data(self, endpoint, data=None):
        return self.__make_post_call(endpoint, data=data)
