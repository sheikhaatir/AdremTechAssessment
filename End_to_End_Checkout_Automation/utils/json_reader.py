import json
import logging
import os

logger = logging.getLogger(__name__)

class JsonReader:
    @staticmethod
    def read_test_data(file_path):
        try:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            full_path = os.path.join(base_dir, file_path)
            with open(full_path, 'r') as f:
                logger.info("Reading test data from %s", full_path)
                return json.load(f)
        except FileNotFoundError:
            logger.error("Test data file not found: %s", full_path)
            raise
        except json.JSONDecodeError as e:
            logger.error("Failed to parse test data: %s", str(e))
            raise