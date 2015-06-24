import b3
import unittest
from common import *

import mock
import time

class TestWait(unittest.TestCase):
    def test_category(self):
        self.assertEqual(b3.Wait.category, b3.ACTION)

    def test_tick(self):
        wait = b3.Wait(milliseconds=15)
        wait.id = 'node1'
        
        _t = time.time()
        tick = TickStub()
        tick.blackboard.get = mock.Mock(side_effect=create_side_effects([
            False,  # is_open inside _open
            _t,     # start_time inside tick
            True,   # is_open inside _open
            _t      # start_time inside tick
        ]))

        status = wait._execute(tick)
        self.assertEqual(status, b3.RUNNING)

        while (time.time()-_t)*1000 < 25: time.sleep(0.01)

        status = wait._execute(tick)
        self.assertEqual(status, b3.SUCCESS)

if __name__ == '__main__':
    unittest.main()