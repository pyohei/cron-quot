import unittest
from cronquot.cronquot import has_directory


class CronquotTest(unittest.TestCase):

    def test_has_directory(self):
        self.assertTrue(has_directory('/tmp'))

if __name__ == '__main__':
    unittest.test()
