import b3
import unittest
from common import *

class TestSucceeder(unittest.TestCase):
    def test_category(self):
        self.assertEqual(b3.Succeeder.category, b3.ACTION)

    def test_tick(self):
        node = b3.Succeeder()
        status = node._execute(TickStub())
        self.assertEqual(status, b3.SUCCESS)

if __name__ == '__main__':
    unittest.main()