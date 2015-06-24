import mock

class TickStub(object):
    def __init__(self):
        self.tree = mock.Mock()
        self.blackboard = mock.Mock()
        self._enter_node = mock.Mock()
        self._open_node = mock.Mock()
        self._tick_node = mock.Mock()
        self._close_node = mock.Mock()
        self._exit_node = mock.Mock()
        self.open_nodes = []
        self.node_count = 0

        self.tree.id = 'tree1'

class NodeStub(object):
    def __init__(self):
        self._execute = mock.Mock()

def create_side_effects(results):
    def function(*args, **kwargs):
        return results.pop(0)
    return function
