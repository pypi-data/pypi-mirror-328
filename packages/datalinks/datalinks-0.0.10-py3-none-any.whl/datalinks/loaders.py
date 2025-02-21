import json
import logging
import pathlib
from abc import ABCMeta, abstractmethod
from typing import List, Dict, Any

_logger = logging.getLogger(__name__)

class Loader(object):
    """
    Abstract base class for loading resources from a specified folder.
    It serves as a template for loading files or other resources
    while maintaining consistency across different implementations.

    :ivar folder: Path to the folder from which resources will be loaded.
    :type folder: pathlib.Path
    """
    __metaclass__ = ABCMeta
    def __init__(self, folder: pathlib.Path):
        self.folder = folder

    @abstractmethod
    def load_from_folder(self): pass


class JSONLoader(Loader):
    """
    A loader for processing JSON files in a specified folder.

    Iterates through all `.json` files within a given folder,
    parses their content, and processes each JSON object into
    a standardized format using the `load_item` method.

    :ivar folder: Path to the folder containing JSON files. All `.json` files
        in this folder will be processed.
    :type folder: Path
    """
    def load_from_folder(self) -> List[Dict[str, str]]:
        _logger.info("Loading json files...")
        rows = []
        # Iterate over all .json files in the folder
        for file_path in self.folder.glob("*.json"):
            _logger.debug(f"Processing: {file_path}: ")
            try:
                # Read the JSON file
                with file_path.open('r', encoding='utf-8') as file:
                    data = json.loads(file.read())

                item = self.load_item(data)
                if item:
                    rows.append(item)
            except json.JSONDecodeError as e:
                _logger.error(f"Error reading JSON from {file_path}: {e}")
        return rows

    @abstractmethod
    def load_item(self, row: Dict[str, Any]) -> Dict[str, str]: pass




