import b3
import unittest

class TestTick(unittest.TestCase):
    def test_initialization(self):
        tick = b3.Tick()
        
        self.assertIsNone(tick.tree)
        self.assertIsNone(tick.debug)
        self.assertIsNone(tick.target)
        self.assertIsNone(tick.blackboard)
        self.assertEqual(tick._node_count, 0)
        self.assertListEqual(tick._open_nodes, [])

    def test_updateTickOnEnter(self):
        tick = b3.Tick()
        node = 'Node'

        tick._enter_node(node)

        self.assertEqual(tick._node_count, 1)
        self.assertListEqual(tick._open_nodes, ['Node'])

    def test_updateTickOnClose(self):
        tick = b3.Tick()
        node = 'Node'

        tick._node_count = 1
        tick._open_nodes = [node]
        tick._close_node(node)

        self.assertEqual(tick._node_count, 1)
        self.assertListEqual(tick._open_nodes, [])

if __name__ == '__main__':
    unittest.main()