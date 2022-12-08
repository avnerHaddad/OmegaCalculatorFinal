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


    def generciLevel(self,level):
        if level == 7:
            return self.__level7()
        head = self.generciLevel(level+1)

        while self.curVal is not None and self.curVal.type in levelDict[level] and self.curVal.type not in PostFixOps:
            type = self.curVal.type
            self.__Next()
            head = TokenNode(head, self.generciLevel(level+1), type)
        return head


    def __level7(self):
        head = self.curVal
        if self.curVal.type == 'BRACKET_OPEN':
            self.__Next()
            head = self.__level1()
            if self.curVal.type != 'BRACKET_CLOSE':
                raise Exception("unclosed bracket error")
            self.__Next()

        elif self.curVal is not None and self.curVal.type in level7:
            type = self.curVal.type
            self.__Next()
            head = TokenNode(head.value, None, type)

        elif self.curVal.type in level1 or self.curVal.type in PostFixOps or self.curVal.type is 'TILDA':
            type = self.curVal.type
            self.__Next()
            return TokenNode(self.__level7(), None, type)
        return head

    def PrintParsed(self):
        self.__printParsedRecursion(self.head)

    def __printParsedRecursion(self, head):
        if head.type != 'NUM':
            print(head.type)
            self.__printParsedRecursion(head.val1)
            self.__printParsedRecursion(head.val2)
            print("did it")
        if head.type == 'NUM':
            print(' val is: ' + str(head.val1))
            print(' val is: ' + str(head.val2))
