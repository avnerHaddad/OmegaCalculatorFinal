from Config import*
class TokenNode:
    def __init__(self, val1, val2, type):
        self.val1 = val1
        self.val2 = val2
        self.type = type

    def calc(self):
        return funcDict[self.type](self.val1, self.val2)


