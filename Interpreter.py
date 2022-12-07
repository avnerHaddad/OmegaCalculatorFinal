from Mparser import Mparser
class Interpreter:
    def __init__(self,str):
        self.parser = Mparser(str)
        self.head = self.parser.head

    def solve(self):
        return self.recursiveSolve(self.head)

    def recursiveSolve(self, head):
        if not isinstance(head.val1, float) and head.val1 is not None:
            head.val1 = self.recursiveSolve(head.val1)
        if not isinstance(head.val2, float) and head.val2 is not None:
            head.val2 = self.recursiveSolve(head.val2)
        return head.calc()
