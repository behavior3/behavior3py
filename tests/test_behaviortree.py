import unittest
import mock

from common import *

import b3

class TestBaseNode(unittest.TestCase):
    def test_initialization(self):
        tree = b3.BehaviorTree()

        self.assertIsNotNone(tree.id)
        self.assertIsNotNone(tree.title)
        self.assertIsNotNone(tree.description)
        self.assertIsNone(tree.root)
        self.assertDictEqual(tree.properties, {})

    def test_callRoot(self):
        tree = b3.BehaviorTree()
        node = mock.Mock()
        blackboard = mock.Mock()
        blackboard.get.return_value = []
        target = {}

        tree.id = 'tree1'
        tree.root = node
        tree.tick(target, blackboard)

        self.assertEqual(node._execute.call_count, 1)
    
    def test_populateBlackboard(self):
        tree = b3.BehaviorTree()
        blackboard = mock.Mock()
        target = {}
        node = mock.Mock()
        

        def side_effect(tick):
            tick._enter_node('node1')
            tick._enter_node('node2')
        node._execute.side_effect = side_effect
        blackboard.get.return_value = []

        tree.id = 'tree1'
        tree.root = node
        tree.tick(target, blackboard)

        expected = [mock.call.get('open_nodes', 'tree1')]
        result = blackboard.get.mock_calls
        self.assertListEqual(result, expected)

        expected = [mock.call.set('open_nodes', ['node1', 'node2'], 'tree1'),
                    mock.call.set('node_count', 2, 'tree1')]
        result = blackboard.set.mock_calls
        self.assertListEqual(result, expected)

    def test_closeOpenedNodes(self):
        tree = b3.BehaviorTree()
        blackboard = mock.Mock()

        node1 = mock.Mock()
        node2 = mock.Mock()
        node3 = mock.Mock()
        node4 = mock.Mock()
        node5 = mock.Mock()
        node6 = mock.Mock()
        node7 = mock.Mock()

        root = mock.Mock()

        def root_side_effect(tick):
            tick._enter_node(node1)
            tick._enter_node(node2)
            tick._enter_node(node3)
        root._execute = mock.Mock()
        root._execute.side_effect = root_side_effect

        def blackboard_side_effect(key, tree_scope=None, node_scope=None):
            if key == 'open_nodes':
                return [node1, node2, node3, node4, node5, node6, node7]
            else:
                return 7
        blackboard.get.side_effect = blackboard_side_effect

        tree.id = 'tree1'
        tree.root = root
        tree.tick(None, blackboard)

        self.assertEqual(node7._close.call_count, 1)
        self.assertEqual(node6._close.call_count, 1)
        self.assertEqual(node5._close.call_count, 1)
        self.assertEqual(node4._close.call_count, 1)
        self.assertEqual(node3._close.call_count, 0)
        self.assertEqual(node2._close.call_count, 0)
        self.assertEqual(node1._close.call_count, 0)



if __name__ == '__main__':
    unittest.main()