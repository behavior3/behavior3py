import unittest
import mock

from common import *

import b3

class TestBaseNode(unittest.TestCase):
    def test_initialization(self):
        node = b3.BaseNode()
        
        self.assertIsNotNone(node.id)
        self.assertIsNone(node.category)
        self.assertIsNotNone(node.title)
        self.assertEqual(node.description, '')
        self.assertDictEqual(node.parameters, {})
        self.assertDictEqual(node.properties, {})
        self.assertEqual(node.description, '')
        self.assertRaises(AttributeError, lambda:node.children)
        self.assertRaises(AttributeError, lambda:node.child)

    def test_openNode(self):
        node = b3.BaseNode()
        tick = TickStub()

        node.id = 'node1'

        # mocking
        tick.blackboard.get.return_value = False
        node._tick = mock.Mock()
        node._tick.return_value = b3.RUNNING # does not close the node

        # run
        node._execute(tick)

        # test
        expected = [mock.call.blackboard.set('is_open', True, 'tree1', 'node1')]
        result = tick.blackboard.set.mock_calls
        
        self.assertListEqual(result, expected)

    def test_closeNode(self):
        node = b3.BaseNode()
        tick = TickStub()

        node.id = 'node1'

        # mocking
        tick.blackboard.get.return_value = True
        node._tick = mock.Mock()
        node._tick.return_value = b3.SUCCESS # close the node

        # run
        node._execute(tick)

        # test
        expected = [mock.call.blackboard.set('is_open', False, 'tree1', 'node1')]
        result = tick.blackboard.set.mock_calls
        
        self.assertListEqual(result, expected)

    def test_executeCallingFunction(self):
        node = b3.BaseNode()
        tick = TickStub()

        node.id = 'node1'

        # mocking
        tick.blackboard.get.return_value = False
        node.enter = mock.Mock()
        node.open = mock.Mock()
        node.tick = mock.Mock()
        node.tick.return_value = b3.SUCCESS # close the node
        node.close = mock.Mock()
        node.exit = mock.Mock()

        # run
        status = node._execute(tick)

        # test
        self.assertIsNotNone(status)
        node.enter.assert_called_once_with(tick)
        node.open.assert_called_once_with(tick)
        node.tick.assert_called_once_with(tick)
        node.close.assert_called_once_with(tick)
        node.exit.assert_called_once_with(tick)

    def test_executeDoesNotOpen(self):
        node = b3.BaseNode()
        tick = TickStub()

        node.id = 'node1'

        # mocking
        tick.blackboard.get.return_value = True
        node._tick = mock.Mock()
        node._tick.return_value = b3.RUNNING # does not close the node

        # run
        node._execute(tick)

        # test
        expected = []
        result = tick.blackboard.set.mock_calls
        
        self.assertListEqual(result, expected)

    def test_executeCallingTickCallbacks(self):
        node = b3.BaseNode()
        tick = TickStub()

        node.id = 'node1'

        # mocking
        tick.blackboard.get.return_value = False
        node.tick = mock.Mock()
        node.tick.return_value = b3.SUCCESS # close the node

        # run
        node._execute(tick)

        tick._enter_node.assert_called_once_with(node)
        tick._open_node.assert_called_once_with(node)
        tick._tick_node.assert_called_once_with(node)
        tick._close_node.assert_called_once_with(node)
        tick._exit_node.assert_called_once_with(node)



if __name__ == '__main__':
    unittest.main()