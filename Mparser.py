from Lexer import Lexer
from TokenNode import TokenNode
from Config import *


class Mparser:

    def __init__(self, str):
        self.lexer = Lexer(str)
        self.index = 0
        self.tokens = self.lexer.GetTokens()
        self.curVal = self.tokens[self.index]
        self.fixPostFixOps()
        self.head = self.Parse()

    # func that calls the recursive decent algorithm
    def Parse(self):
        head = self.generciLevel(1)
        return head

# updates the value of curVal to what the current index is pointing to
    def __Updatecur(self):
        try:
            self.curVal = self.tokens[self.index]
        except IndexError:
            self.curVal = None

# advances the index one step forward and updates curVal on the way, raises exception if not possible
    def __Next(self):
        try:
            self.index += 1
            self.curVal = self.tokens[self.index]
        except IndexError:
            self.curVal = None

    # steps one step backward with index and updates curVal on the way, raises exception if not possible
    def __Back(self):
        try:
            self.index -= 1
            self.curVal = self.tokens[self.index]
        except IndexError:
            self.curVal = None

    def __curVal(self):
        if self.index >= len(self.tokens):
            return None
        else:
            return self.tokens[self.index]

# func that goes over the current tkens and moves back all of the postfix operators to where they should have been
    # operated lineraly
    def fixPostFixOps(self):
        while self.curVal is not None:
            if self.curVal.type in PostFixOps:
                toSwtich = self.tokens.pop(self.index)
                self.__Back()
                if self.curVal.type not in digs and self.curVal.type not in brackets:
                    raise Exception("post fix operator with no number before to operate on")
                if self.curVal.type in brackets:
                    while self.curVal.type is not 'BRACKET_OPEN':
                        self.__Back()

                while self.index > 0 and TokenPowerDict[self.prevVal().type] >= TokenPowerDict[toSwtich.type]:
                    self.__Back()
                self.tokens.insert(self.index, toSwtich)
                self.NextNonePostFix()
            self.__Next()
        self.index = 0
        self.__Updatecur()

# helper function for fixPostFixOps moves the index to the next non post fix object
    def NextNonePostFix(self):
        while self.curVal.type in PostFixOps:
            self.__Next()

# the main parsing algorithm, calls itself recursively, returns a head of a miniTree of the specific operators(based
    # on levels of strength) until it reaches a number and returns a number node
    def generciLevel(self, level):
        if level == finalLevel:
            return self.finalLevel()
        head = self.generciLevel(level + 1)

        while self.curVal is not None and self.curVal.type in levelDict[level] and self.curVal.type not in PostFixOps:
            type = self.curVal.type
            self.__Next()
            head = TokenNode(head, self.generciLevel(level + 1), type)
        return head

# the final part of the previous function, handles the specifics such as SingledigOps, Brackets and Nums
    def finalLevel(self):
        head = self.curVal
        if self.curVal.type == 'BRACKET_OPEN':
            self.__Next()
            head = self.generciLevel(1)
            if self.curVal.type != 'BRACKET_CLOSE':
                raise Exception("unclosed bracket error")
            self.__Next()

        elif self.curVal is not None and self.curVal.type in level7:
            type = self.curVal.type
            self.__Next()
            head = TokenNode(head.value, None, type)

        elif self.curVal.type in SingleDigOps:
            type = self.curVal.type
            self.__Next()
            return TokenNode(self.finalLevel(), None, type)
        else:
            raise Exception("operator invalid in currrent index")

        return head

# returns the value at the index before if possible, like Back but without decreasing index
    def prevVal(self):
        if self.index > 0:
            return self.tokens[self.index - 1]
        else:
            raise Exception("error")
