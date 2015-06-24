import b3

__all__ = ['Inverter']

class Inverter(b3.Decorator):
    def tick(self, tick):
        if not self.child:
            return b3.ERROR

        status = self.child._execute(tick)

        if status == b3.SUCCESS:
            status = b3.FAILURE
        elif status == b3.FAILURE:
            status = b3.SUCCESS

        return status
        
