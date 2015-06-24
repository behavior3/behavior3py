import b3
import unittest
from common import *

def get_node(status):
    stub = NodeStub();
    stub._execute.return_value = status
    return stub

class TestSequence(unittest.TestCase):
    def test_category(self):
        self.assertEqual(b3.Sequence.category, b3.COMPOSITE)

    def test_initialization(self):
        node = b3.Sequence()

        self.assertIsNotNone(node.id)
        self.assertEqual(node.name, 'Sequence')
        self.assertEqual(node.title, 'Sequence')
        self.assertIsNotNone(node.description)

    def test_success(self):
        node1 = get_node(b3.SUCCESS)
        node2 = get_node(b3.SUCCESS)
        node3 = get_node(b3.SUCCESS)

        sequence = b3.Sequence(children=[node1, node2, node3])
        status = sequence.tick(TickStub())

        self.assertEqual(status, b3.SUCCESS)
        self.assertEqual(node1._execute.call_count, 1)
        self.assertEqual(node2._execute.call_count, 1)
        self.assertEqual(node3._execute.call_count, 1)

    def test_failure(self):
        node1 = get_node(b3.SUCCESS)
        node2 = get_node(b3.SUCCESS)
        node3 = get_node(b3.FAILURE)
        node4 = get_node(b3.SUCCESS)

        sequence = b3.Sequence(children=[node1, node2, node3, node4])
        status = sequence.tick(TickStub())

        self.assertEqual(status, b3.FAILURE)
        self.assertEqual(node1._execute.call_count, 1)
        self.assertEqual(node2._execute.call_count, 1)
        self.assertEqual(node3._execute.call_count, 1)
        self.assertEqual(node4._execute.call_count, 0)

    def test_running(self):
        node1 = get_node(b3.SUCCESS)
        node2 = get_node(b3.SUCCESS)
        node3 = get_node(b3.RUNNING)
        node4 = get_node(b3.SUCCESS)

        sequence = b3.Sequence(children=[node1, node2, node3, node4])
        status = sequence.tick(TickStub())

        self.assertEqual(status, b3.RUNNING)
        self.assertEqual(node1._execute.call_count, 1)
        self.assertEqual(node2._execute.call_count, 1)
        self.assertEqual(node3._execute.call_count, 1)
        self.assertEqual(node4._execute.call_count, 0)

    def test_error(self):
        node1 = get_node(b3.SUCCESS)
        node2 = get_node(b3.SUCCESS)
        node3 = get_node(b3.ERROR)
        node4 = get_node(b3.SUCCESS)

        sequence = b3.Sequence(children=[node1, node2, node3, node4])
        status = sequence.tick(TickStub())

        self.assertEqual(status, b3.ERROR)
        self.assertEqual(node1._execute.call_count, 1)
        self.assertEqual(node2._execute.call_count, 1)
        self.assertEqual(node3._execute.call_count, 1)
        self.assertEqual(node4._execute.call_count, 0)


if __name__ == '__main__':
    unittest.main()