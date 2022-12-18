from Mparser import Mparser
from Exceptions import *


class Interpreter:
    def __init__(self, str):
        self.parser = Mparser(str)
        self.head = None

    # func that calls the recursive solver
    def solve(self):
        self.head = self.parser.Parse()
        return self.recursiveSolve(self.head)

    # solves the binary tree that was generated from the parser, scans tree untl reaches final leaf then calculates
    # back up using the internal calc method of each node
    def recursiveSolve(self, head):
        if not isinstance(head.val1, float) and head.val1 is not None:
            head.val1 = self.recursiveSolve(head.val1)
        if not isinstance(head.val2, float) and head.val2 is not None:
            head.val2 = self.recursiveSolve(head.val2)
        return head.calc()
