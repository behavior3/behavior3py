import b3
import unittest

class TestComposite(unittest.TestCase):
    def test_category(self):
        self.assertEqual(b3.Decorator.category, b3.DECORATOR)

    def test_initialization(self):
        node = b3.Decorator(child='child1')

        self.assertIsNotNone(node.child)
        self.assertEqual(node.child, 'child1')

if __name__ == '__main__':
    unittest.main()