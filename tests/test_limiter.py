import b3
import unittest
from common import *

class TestLimiter(unittest.TestCase):
    def test_category(self):
        self.assertEqual(b3.Limiter.category, b3.DECORATOR)

    def test_limit(self):
        node = NodeStub()
        limiter = b3.Limiter(node, max_loop=10)
        tick = TickStub()
        
        tick.blackboard.get = mock.Mock(side_effect=create_side_effects([False, 0]))
        limiter._execute(tick)
        self.assertEqual(node._execute.call_count, 1)

        tick.blackboard.get = mock.Mock(side_effect=create_side_effects([False, 10]))
        limiter._execute(tick)
        self.assertEqual(node._execute.call_count, 1)

    def test_running_doesnt_count(self):
        node = NodeStub()
        limiter = b3.Limiter(node, max_loop=10)
        tick = TickStub()
        
        tick.blackboard.get = mock.Mock(side_effect=create_side_effects([False, 0]))
        limiter._execute(tick)
        self.assertEqual(node._execute.call_count, 1)
        



if __name__ == '__main__':
    unittest.main()