from Lexer import Lexer
from TokenNode import TokenNode
from Config import *


class Mparser:

    def __init__(self, str):
        self.lexer = Lexer(str)
        self.index = 0
        self.tokens = self.lexer.GetTokens()
        self.curVal = self.tokens[self.index]
        self.head = self.Parse()
        self.fixPostFixOps()

    def Parse(self):
        head = self.generciLevel(1)
        return head


    def __Updatecur(self):
        try:
            self.curVal = self.tokens[self.index]
        except IndexError:
            self.curVal = None

    def __Next(self):
        try:
            self.index += 1
            self.curVal = self.tokens[self.index]
        except IndexError:
            self.curVal = None

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
                if self.index >0:
                    self.__Back()

                while \
                        TokenPowerDict[self.curVal.type] >= TokenPowerDict[
                            toSwtich.type] and self.curVal.type not in digs and self.index is not 0 and self.curVal.type in SingleDigOps:
                    self.__Back()
                self.tokens.insert(self.index, toSwtich)
                self.__Next()
            self.__Next()
        self.index = 0
        self.__Updatecur()
    def generciLevel(self,level):
        if level == finalLevel:
            return self.finalLevel()
        head = self.generciLevel(level+1)

        while self.curVal is not None and self.curVal.type in levelDict[level] and self.curVal.type not in PostFixOps:
            type = self.curVal.type
            self.__Next()
            head = TokenNode(head, self.generciLevel(level+1), type)
        return head


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
        return head


