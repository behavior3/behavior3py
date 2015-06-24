import b3
import unittest

class TestCondition(unittest.TestCase):
    def test_category(self):
        self.assertEqual(b3.Condition.category, b3.CONDITION)

if __name__ == '__main__':
    unittest.main()