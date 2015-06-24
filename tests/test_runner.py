import b3
import unittest
from common import *

class TestRunner(unittest.TestCase):
    def test_category(self):
        self.assertEqual(b3.Runner.category, b3.ACTION)

    def test_tick(self):
        node = b3.Runner()
        status = node._execute(TickStub())
        self.assertEqual(status, b3.RUNNING)

if __name__ == '__main__':
    unittest.main()