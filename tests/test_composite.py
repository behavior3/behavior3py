import b3
import unittest

class TestComposite(unittest.TestCase):
    def test_category(self):
        self.assertEqual(b3.Composite.category, b3.COMPOSITE)

    def test_initialization(self):
        node = b3.Composite(children=['child1', 'child2'])

        self.assertIsNotNone(node.children)
        self.assertEqual(node.children[0], 'child1')
        self.assertEqual(node.children[1], 'child2')

if __name__ == '__main__':
    unittest.main()