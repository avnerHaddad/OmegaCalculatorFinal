from Lexer import Lexer
from TokenNode import TokenNode
from Config import *


class Mparser:

    def __init__(self, str):
        self.lexer = Lexer(str)
        self.index = 0
        self.tokens = self.lexer.GetTokens()
        self.head = self.Parse()

    def Parse(self):
        head = self.__level1()
        return head

    def __Next(self):
        try:
            self.index += 1
            self.tokens[self.index]
        except IndexError:
            pass

    def __curVal(self):
        if self.index >= len(self.tokens):
            return None
        else:
            return self.tokens[self.index]

    def __level1(self):
        head = self.__level2()

        while self.__curVal() is not None and self.__curVal().type in level1:
            type = self.__curVal().type
            self.__Next()
            head = TokenNode(head, self.__level2(), type)
        return head

    def __level2(self):
        head = self.__level3()

        while self.__curVal() is not None and self.__curVal().type in level2:
            type = self.__curVal().type
            self.__Next()
            head = TokenNode(head, self.__level2(), type)
        return head

    def __level3(self):
        head = self.__level4()

        while self.__curVal() is not None and self.__curVal().type in level3:
            type = self.__curVal().type
            self.__Next()
            head = TokenNode(head, self.__level4(), type)
        return head

    def __level4(self):
        head = self.__level5()

        while self.__curVal() is not None and self.__curVal().type in level4:
            type = self.__curVal().type
            self.__Next()
            head = TokenNode(head, self.__level5(), type)
        return head

    def __level5(self):
        head = self.__level6()

        while self.__curVal() is not None and self.__curVal().type in level5:
            type = self.__curVal().type
            self.__Next()
            head = TokenNode(head, self.__level6(), type)
        return head

    def __level6(self):
        head = self.__level7()

        while self.__curVal() is not None and self.__curVal().type in level6:
            type = self.__curVal().type
            self.__Next()
            head = TokenNode(head, self.__level7(), type)
        return head

    def __level7(self):
        head = self.__curVal()
        if self.__curVal().type == 'BRACKET_OPEN':
            self.__Next()
            head = self.__level1()
            if self.__curVal().type != 'BRACKET_CLOSE':
                raise Exception("unclosed bracket error")
            self.__Next()

        elif self.__curVal() is not None and self.__curVal().type in level7:
            type = self.__curVal().type
            self.__Next()
            head = TokenNode(head.value, None, type)
        elif self.__curVal().type in level1:
            type = self.__curVal().type
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
