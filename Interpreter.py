from Mparser import Mparser
class Interpreter:
    def __init__(self,str):
        self.parser = Mparser(str)
        self.head = self.parser.head

    def Solve(self):
        return self.RecursiveSolve(self.head)

    def RecursiveSolve(self,head):
        if(not isinstance(head.val1,float) and head.val1 != None):
            head.val1 = self.RecursiveSolve(head.val1)
        if (not isinstance(head.val2, float) and head.val2 != None ):
            head.val2 = self.RecursiveSolve(head.val2)
        return head.calc()

