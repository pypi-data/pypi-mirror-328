import requests
import pandas as pd
from typing import Union, List
import logging
from requests.exceptions import HTTPError

# Configure logging to output messages to the console
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ResourceProxy:
    def __init__(self, client, resource_type):
        """
        Initialize the ResourceProxy with a client and resource type.
        The client is an instance of APIClient, and resource_type is a string
        representing the type of resource (e.g., 'users', 'stations').
        """
        self.client = client
        self.resource_type = resource_type

    def all(self) -> pd.DataFrame:
        """
        Fetch all resources of the specified type.
        Returns a DataFrame containing all resources.
        """
        try:
            return self.client.get(f'/{self.resource_type}')
        except Exception as e:
            logger.error(f"Error fetching all resources: {e}")
            raise

    def get(self, id: Union[int, str]) -> pd.DataFrame:
        """
        Fetch a single resource by its ID.
        Returns a DataFrame containing the resource.
        """
        try:
            return self.client.get(f'/{self.resource_type}/{id}')
        except Exception as e:
            logger.error(f"Error fetching resource with ID {id}: {e}")
            raise

    def filter(self, **kwargs) -> pd.DataFrame:
        """
        Filter resources by query parameters.
        Returns a DataFrame containing the filtered resources.
        """
        try:
            return self.client.get(f'/{self.resource_type}', params=kwargs)
        except Exception as e:
            logger.error(f"Error filtering resources: {e}")
            raise

    def exclude(self, ids: List[int]) -> pd.DataFrame:
        """
        Fetch all resources excluding those with the specified IDs.
        Returns a DataFrame containing the remaining resources.
        """
        try:
            all_resources = self.all()
            return all_resources[~all_resources['id'].isin(ids)]
        except Exception as e:
            logger.error(f"Error excluding resources: {e}")
            raise

class APIClient:
    def __init__(self, base_url='http://localhost:3000', token=None, timeout=30):
        """
        Initialize the APIClient with a base URL and optional token.
        The base URL is the root endpoint of the API.
        The token is used for authentication.
        """
        self.base_url = base_url
        self.headers = {'Content-Type': 'application/json'}
        if token:
            self.headers['Authorization'] = f'Bearer {token}'
        self.timeout = timeout
        self.session = requests.Session()

        # Initialize resource proxies for different types of resources
        self.user = ResourceProxy(self, 'users')
        self.station = ResourceProxy(self, 'stations')
        self.project = ResourceProxy(self, 'projects')
        self.sensor_type = ResourceProxy(self, 'sensor-types')
        self.datalogger_station_mapping = ResourceProxy(self, 'datalogger-station-mapping')
        self.station_sensor_order = ResourceProxy(self, 'station-sensor-order')
        self.processed_file = ResourceProxy(self, 'processed-files')
        self.station_note = ResourceProxy(self, 'station-notes')
        self.sensor_reading = ResourceProxy(self, 'sensor-readings')

    def get(self, endpoint, params=None) -> pd.DataFrame:
        """
        Make a GET request to the API.
        Returns a DataFrame containing the response data.
        """
        url = f'{self.base_url}{endpoint}'
        try:
            response = self.session.get(url, headers=self.headers, params=params, timeout=self.timeout)
            response.raise_for_status()
            return pd.json_normalize(response.json())
        except HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            logger.error(f"Other error occurred: {err}")
            raise

    def post(self, endpoint, data) -> dict:
        """
        Make a POST request to the API.
        Returns the JSON response from the API.
        """
        url = f'{self.base_url}{endpoint}'
        try:
            response = self.session.post(url, headers=self.headers, json=data, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            logger.error(f"Other error occurred: {err}")
            raise

    def patch(self, endpoint, data) -> dict:
        """
        Make a PATCH request to the API.
        Returns the JSON response from the API.
        """
        url = f'{self.base_url}{endpoint}'
        try:
            response = self.session.patch(url, headers=self.headers, json=data, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            logger.error(f"Other error occurred: {err}")
            raise

    def delete(self, endpoint) -> int:
        """
        Make a DELETE request to the API.
        Returns the HTTP status code of the response.
        """
        url = f'{self.base_url}{endpoint}'
        try:
            response = self.session.delete(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            return response.status_code
        except HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            logger.error(f"Other error occurred: {err}")
            raise

    def login(self, email: str, password: str) -> None:
        """
        Authenticate with the API using an email and password.
        Stores the JWT token in the headers for future requests.
        """
        data = {"email": email, "password": password}
        try:
            response = self.session.post(f'{self.base_url}/auth/login', json=data, timeout=self.timeout)
            response.raise_for_status()
            token = response.json().get('token')
            if token:
                self.headers['Authorization'] = f'Bearer {token}'
                print(token)  # Print the token for verification
        except HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
            raise ConnectionError("Invalid credentials. Please check your email and password.")
        except Exception as err:
            logger.error(f"Other error occurred: {err}")
            raise ConnectionError("Invalid credentials. Please check your email and password.")

    def close(self):
        """
        Close the session to free up system resources.
        """
        self.session.close()

    def __enter__(self):
        """
        Enter the runtime context related to this object.
        The with statement binds this method's return value to the target specified in the as clause of the statement.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the runtime context related to this object.
        The parameters describe the exception that caused the context to be exited.
        """
        self.close()

# Example usage
if __name__ == "__main__":
    with APIClient(base_url="http://localhost:3000") as client:  # Change to your API URL
        client.login(email="john@example.com", password="secret")  # Change to your email and password

        # Get all users
        users = client.user.all()
        print("All users:\n", users)

        # Get users from ID 1 to 10
        users_range = client.user.all()[1:11]
        print("Users from 1 to 10:\n", users_range)

        # Exclude users with IDs 7, 8, 9
        users_excluded = client.user.exclude([7, 8, 9])
        print("Users excluding 7, 8, 9:\n", users_excluded)

        # Filter stations by date range
        stations = client.station.filter(start_date="2025-01-01", end_date="2025-12-31")
        print("Stations from 2025-01-01 to 2025-12-31:\n", stations)
