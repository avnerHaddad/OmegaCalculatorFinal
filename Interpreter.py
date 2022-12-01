from Mparser import Mparser
class Interpreter:
    def __init__(self,str):
        self.parser = Mparser(str)
        self.head = self.parser.head

    def Solve(self):
        pass