from Mparser import Mparser
from Exceptions import *


class OmegaMathInterpreter:
    def __init__(self):
        self.parser = Mparser()
        self.head = None

    # func that calls the recursive solver
    def solve(self,inputString):
        self.head = self.parser.Parse(inputString)
        return round(self.recursiveSolve(self.head), 10)

    # solves the binary tree that was generated from the parser, scans tree until reaches final leaf then calculates
    # back up using the internal calc method of each node
    def recursiveSolve(self, head):
        if not isinstance(head.val1, float) and head.val1 is not None:
            head.val1 = self.recursiveSolve(head.val1)
        if not isinstance(head.val2, float) and head.val2 is not None:
            head.val2 = self.recursiveSolve(head.val2)
        return head.calc()
