import b3
import unittest
from common import *

class TestError(unittest.TestCase):
    def test_category(self):
        self.assertEqual(b3.Error.category, b3.ACTION)

    def test_tick(self):
        node = b3.Error()
        status = node._execute(TickStub())
        self.assertEqual(status, b3.ERROR)

if __name__ == '__main__':
    unittest.main()