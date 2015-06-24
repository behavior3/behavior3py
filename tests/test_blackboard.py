import unittest
import mock

from common import *

import b3

class TestBaseNode(unittest.TestCase):
    def test_basicReadAndWrite(self):
        blackboard = b3.Blackboard()

        blackboard.set('var1', 'string')
        blackboard.set('var2', 100)

        self.assertEqual(blackboard.get('var1'), 'string')
        self.assertEqual(blackboard.get('var2'), 100)

    def test_treeMemoryInitialization(self):
        blackboard = b3.Blackboard()

        blackboard.set('var1', 'value', 'tree1')

        self.assertIsNotNone(blackboard.get('var1', 'tree1'))
        self.assertIsNotNone(blackboard.get('node_memory', 'tree1'))
        self.assertIsNotNone(blackboard.get('open_nodes', 'tree1'))

    def test_readAndWriteWithinTreeScope(self):
        blackboard = b3.Blackboard()

        blackboard.set('var1', 'string', 'tree1')
        blackboard.set('var2', 100, 'tree2')

        self.assertEqual(blackboard.get('var1', 'tree1'), 'string')
        self.assertEqual(blackboard.get('var2', 'tree2'), 100)

        self.assertEqual(blackboard.get('var1', 'tree2'), None)
        self.assertEqual(blackboard.get('var2', 'tree1'), None)

    def test_readAndWriteWithinNodeScope(self):
        blackboard = b3.Blackboard()


        blackboard.set('var1', 'value 1', 'tree 1')
        blackboard.set('var2', 'value 2', 'tree 1', 'node 1')
        blackboard.set('var3', 'value 3', 'tree 1', 'node 2')
        blackboard.set('var4', 1000, 'tree 2')

        self.assertEqual(blackboard.get('var2', 'tree 1', 'node 1'), 'value 2');
        self.assertEqual(blackboard.get('var3', 'tree 1', 'node 2'), 'value 3');
        self.assertEqual(blackboard.get('var2', 'tree 1', 'node 2'), None);
        self.assertEqual(blackboard.get('var3', 'tree 1', 'node 1'), None);
        self.assertEqual(blackboard.get('var2', 'tree 1'), None);
        self.assertEqual(blackboard.get('var1', 'tree 1', 'node 1'), None);
        self.assertEqual(blackboard.get('var2', 'tree 2', 'node 1'), None);

if __name__ == '__main__':
    unittest.main()