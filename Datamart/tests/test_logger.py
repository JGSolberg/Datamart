import unittest
import logging
import io
import sys
from logger.logging_config import setup_logging

class TestLogging(unittest.TestCase):

    def setUp(self):
        self.log_output = io.StringIO()
        handler = logging.StreamHandler(self.log_output)
        logging.getLogger().addHandler(handler)
        logging.getLogger().setLevel(logging.DEBUG)
    
    def test_logging(self):
        setup_logging('test_log', True)
        logging.info('This is an info message')
        log_contents = self.log_output.getvalue()
        self.assertIn('INFO - This is an info message', log_contents)

if __name__ == '__main__':
    unittest.main()
