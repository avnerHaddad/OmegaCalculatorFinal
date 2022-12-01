from Lexer import Lexer
from TokenNode import TokenNode
from Config import *
class Parser:

    def __int__(self, input):
        self.lexer = Lexer(input)
        self.index = 0
        self.tokens = self.lexer.GetTokens()

    def Parse(self):
        return self.__level1()
        pass


    def __Next(self):
        self.index += 1

    def __curVal(self):
        self.tokens[self.index]


    def __level1(self):
        head = self.__level2()

        while(self.__curVal() != None and self.__curVal() in level1):
            type = self.__curVal().type
            self.__Next()
            head = TokenNode(head, self.__level2(), type)
        return head

    def __level2(self):
        head = self.__level3()

        while (self.__curVal() != None and self.__curVal() in level2):
            type = self.__curVal().type
            self.__Next()
            head = TokenNode(head, self.__level2(), type)
        return head

    def __level3(self):
        head = self.__level4()

        while (self.__curVal() != None and self.__curVal() in level3):
            type = self.__curVal().type
            self.__Next()
            head = TokenNode(head, self.__level4(), type)
        return head


    def __level4(self):
        head = self.__level5()

        while (self.__curVal() != None and self.__curVal() in level4):
            type = self.__curVal().type
            self.__Next()
            head = TokenNode(head, self.__level5(), type)
        return head


    def __level5(self):
        head = self.__level6()

        while (self.__curVal() != None and self.__curVal() in level5):
            type = self.__curVal().type
            self.__Next()
            head = TokenNode(head, self.__level6(), type)
        return head


    def __level6(self):
        head = self.__level7()

        while (self.__curVal() != None and self.__curVal() in level6):
            type = self.__curVal().type
            self.__Next()
            head = TokenNode(head, self.__level7(), type)
        return head


    def __level7(self):
        pass