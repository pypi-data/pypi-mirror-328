import functools
import logging
import os
from dataclasses import dataclass
from typing import List, Dict, Any, Optional, Type

import requests
from requests import Response
import dotenv

from datalinks.chain import Chain
from datalinks.links import MatchTypeConfig

_logger = logging.getLogger(__name__)

TIMEOUT = 3400
MAX_INGEST_ATTEMPTS = 3


@dataclass
class DLConfig:
    """
    DLConfig class is a configuration container for managing the required settings
    to interact with DataLinks. It loads configuration values from environment
    variables to provide flexibility across different environments.

    This class is designed to simplify the initialization and storage of connection
    and namespace details required to communicate with DataLinks.

    :ivar host: The host URL for the data layer connection.
    :type host: str
    :ivar apikey: The API key for authentication with the data layer.
    :type apikey: str
    :ivar index: The index name to be used in the data layer operations.
    :type index: str
    :ivar namespace: The namespace for organizing data in the data layer.
    :type namespace: str
    :ivar objectname: The name of the object associated with the configuration.
                      Defaults to an empty string.
    :type objectname: str
    """
    host: str
    apikey: str
    index: str
    namespace: str
    objectname: str = ""

    @classmethod
    def from_env(cls: Type["DLConfig"], load_dotenv: bool = True):
        if load_dotenv: dotenv.load_dotenv()
        return cls(
            host=os.getenv("HOST", "host-notset"),
            apikey=os.getenv("DL_API_KEY", "api-key-notset"),
            index=os.getenv("INDEX", "index-notset"),
            namespace=os.getenv("NAMESPACE", "namespace-notset"),
            objectname=os.getenv("OBJECT_NAME", ""),
        )


@dataclass
class IngestionResult:
    """
    Represents the result of a data ingestion process into DataLinks.

    This class is a data structure used to store the results of a data ingestion
    operation. It separates the successfully ingested items from the failed ones,
    enabling users to track and handle both cases effectively.

    :ivar successful: A list of records successfully ingested. Each record is
        represented as a dictionary.
    :type successful: List[Dict[str, Any]]
    :ivar failed: A list of records that failed ingestion. Each record is
        represented as a dictionary.
    :type failed: List[Dict[str, Any]]
    """
    successful: List[Dict[str, Any]]
    failed: List[Dict[str, Any]]


class DataLinksAPI:
    """
    Class for interfacing with the DataLinks API.

    Provides methods for ingesting data, managing namespaces, and querying data
    from DataLinks. Designed to interact with a configurable
    backend, providing flexibility for deployment environments.

    :ivar config: Configuration object containing API key, host, index, namespace,
        and object name.
    :type config: Optional[DLConfig]
    """
    def __init__(self, config: Optional[DLConfig] = None):
        self.config = config if config else DLConfig.from_env()
        self.__headers = {"Authorization": f"Bearer {self.config.apikey}"}
        self.__ingest_url = f"{self.config.host}/ingest/{self.config.index}/{self.config.namespace}/{self.config.objectname}"
        self.__create_url = f"{self.config.host}/ingest/new/{self.config.namespace}/{self.config.objectname}"
        self.__data_url = f"{self.config.host}/data/self/{self.config.namespace}/{self.config.objectname}"

    def __post_request(self, payload: str | Dict[str, Any], endpoint: str) -> Response:
        try:
            post_template = functools.partial(
                requests.post,
                url=endpoint,
                timeout=TIMEOUT,
                headers=self.__headers
            )
            if isinstance(payload, dict):
                response = post_template(json = payload)
            else:
                response = post_template(data = payload)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            if e.response and e.response.status_code != 409:
                _logger.error(f"Request to {endpoint} failed: {e}")
            raise

    def __get_request(self, endpoint: str) -> Response:
        try:
            response = requests.get(
                endpoint,
                timeout=TIMEOUT,
                headers=self.__headers
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            _logger.error(f"Request to {endpoint} failed: {e}")
            raise

    def ingest(self, data: List[Dict],
               inference_steps: Chain,
               entity_resolution: MatchTypeConfig,
               batch_size=0,
               max_attempts=MAX_INGEST_ATTEMPTS) -> IngestionResult:
        """
        Ingests data into the namespace by batching the given data and performing multiple retries
        in case of failures. This function sends data in chunks (batches), to be processed through configured
        inference steps, and to resolve entities based on the provided configuration. If a batch fails, it
        is retried up to a maximum number of attempts.

        :param data: List of dictionaries, where each dictionary represents a data block to be ingested.
        :param inference_steps: Chain of inference steps to be applied for processing the data.
        :param entity_resolution: Configuration specifying how entity resolution is to be performed.
        :param batch_size: Number of data blocks to be included in each batch. Defaults to the size of the
            entire dataset if not provided.
        :param max_attempts: Maximum number of retry attempts for failed batches. Defaults to the
            provided constant MAX_INGEST_ATTEMPTS.
        :return: An IngestionResult object containing lists of successfully ingested data blocks and
            data blocks that failed to be ingested.
        """
        if not batch_size:
            batch_size = len(data)
        _logger.info(f"Sending {len(data)} data blocks to ingestion endpoint (batch size {batch_size})")

        retry_data: List[Dict[str, Any]] = []
        successful_batches = []

        for attempt in range(max_attempts):
            _logger.debug(f"Attempt {attempt + 1} of {max_attempts}")
            retry_data = []

            for start in range(0, len(data), batch_size):
                batch = data[start:start + batch_size]
                payload = {
                    "data": batch,
                    "infer": {"steps": inference_steps.to_list()},
                    "link": entity_resolution.config,
                }
                try:
                    response = self.__post_request(payload, self.__ingest_url)
                    if response.status_code == 200:
                        successful_batches.extend(batch)

                    else:
                        _logger.error(f"Batch failed with status {response.status_code}")
                        retry_data.extend(batch)
                except requests.exceptions.RequestException as e:
                    _logger.error(f"Batch failed: {e}")
                    retry_data.extend(batch)

            if retry_data:
                data = retry_data
            else:
                break

        return IngestionResult(
            successful=successful_batches,
            failed=retry_data
        )

    def create_space(self, is_private: bool = True) -> None:
        """
        Creates a new space with the specified privacy settings. This function sends a
        POST request to create a namespace with the given privacy status. Information
        about the namespace creation will be logged, including the HTTP status code
        and response reason. If the namespace already exists, a warning will be logged.

        :param is_private: Determines whether the created namespace will be private
            or public.
        :type is_private: bool
        :return: None
        :raises HTTPError: If the HTTP request fails due to connectivity issues or
            server-side problems.
        """
        payload = {"isPrivate": is_private}
        try:
            response = self.__post_request(payload, self.__create_url)

            _logger.info(f"Namespace creation (private: {is_private}) | "
                         f"{response.status_code} | {response.reason}")
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 409:
                _logger.warning(f"Space {self.__create_url} already exists")
            else:
                _logger.error("Failed to create space")

    def query_data(self, query: str = "*", include_metadata: bool = False) -> List[Dict] | None:
        """
        Queries data from a specified data source and processes the response.

        The method allows querying with a specific query string or with a wildcard
        ("*") for all data. The response from the query can be filtered to exclude
        metadata fields if `include_metadata` is set to False. Metadata fields are
        identified by key names starting with an underscore.

        :param query: The query string to use for fetching data. Defaults to "*",
                      which retrieves all data.
        :type query: str
        :param include_metadata: Specifies whether to include metadata fields in
                                 the returned data. Defaults to False.
        :type include_metadata: bool
        :return: A list of records represented as dictionaries, or None if the query
                 fails or an exception occurs during the request.
        :rtype: List[Dict] | None
        :raises requests.exceptions.RequestException: If a request-related error
            occurs during querying.
        """
        jsondata: List[Dict[str, Any]] = []
        try:
            response = self.__post_request(query, self.__data_url)
            if response.status_code == 200:
                jsondata = response.json()
            else:
                _logger.error(f"Query data failed with status {response.status_code}")
        except requests.exceptions.RequestException as e:
            _logger.error(f"Query data failed: {e}")

        if jsondata and not include_metadata:
            return [dict(filter(lambda key_value: not str(key_value[0]).startswith("_"),
                                record.items()))
                    for record in jsondata]
        return jsondata
