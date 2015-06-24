import b3
import unittest

class TestAction(unittest.TestCase):
    def test_category(self):
        self.assertEqual(b3.Action.category, b3.ACTION)

if __name__ == '__main__':
    unittest.main()