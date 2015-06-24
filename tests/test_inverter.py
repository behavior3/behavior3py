import b3
import unittest
from common import *

class TestInverter(unittest.TestCase):
    def test_category(self):
        self.assertEqual(b3.Inverter.category, b3.DECORATOR)

    def test_success(self):
        node = NodeStub()
        inverter = b3.Inverter(node)
        tick = TickStub()

        node._execute.return_value = b3.SUCCESS
        status = inverter._execute(tick)
        self.assertEqual(status, b3.FAILURE)

    def test_failure(self):
        node = NodeStub()
        inverter = b3.Inverter(node)
        tick = TickStub()

        node._execute.return_value = b3.FAILURE
        status = inverter._execute(tick)
        self.assertEqual(status, b3.SUCCESS)

    def test_running(self):
        node = NodeStub()
        inverter = b3.Inverter(node)
        tick = TickStub()

        node._execute.return_value = b3.RUNNING
        status = inverter._execute(tick)
        self.assertEqual(status, b3.RUNNING)

    def test_running(self):
        inverter = b3.Inverter()
        tick = TickStub()

        status = inverter._execute(tick)
        self.assertEqual(status, b3.ERROR)


if __name__ == '__main__':
    unittest.main()