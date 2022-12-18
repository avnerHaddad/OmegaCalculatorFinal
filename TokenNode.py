from Config import *


class TokenNode:
    def __init__(self, val1, val2, type):
        self.val1 = val1
        self.val2 = val2
        self.type = type

    # func that executes the func for the corresponding operator type of the token using the dictionary
    def calc(self):
        return funcDict[self.type](self.val1, self.val2)

