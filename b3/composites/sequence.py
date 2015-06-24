import b3

__all__ = ['Sequence']

class Sequence(b3.Composite):

    def __init__(self, children=None):
        super(Sequence, self).__init__(children)

    def tick(self, tick):
        for node in self.children:
            status = node._execute(tick)

            if status != b3.SUCCESS:
                return status

        return b3.SUCCESS
