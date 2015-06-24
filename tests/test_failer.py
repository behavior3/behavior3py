import b3
import unittest
from common import *

class TestFailer(unittest.TestCase):
    def test_category(self):
        self.assertEqual(b3.Failer.category, b3.ACTION)

    def test_tick(self):
        node = b3.Failer()
        status = node._execute(TickStub())
        self.assertEqual(status, b3.FAILURE)

if __name__ == '__main__':
    unittest.main()