import unittest

from tools.get_logger import GetLogger

logger = GetLogger().get_logger()

class TestLog(unittest.TestCase):
    def test_log(self):
        logger.debug("debug")
        logger.info("info")
        logger.error("error")