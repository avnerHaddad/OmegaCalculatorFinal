from Config import TokenDict, digs
from Token import Token


class Lexer:
    def __init__(self, equation):
        self.equation = equation
        self.iterator = 0
        self.tokens = []

    def __insertToken(self, TYPE, value=None):
        self.tokens.append(Token(TYPE, value))

    def __getTokens(self):
        while self.iterator < len(self.equation):
            if self.__ValAt() in digs:
                self.__getNumberToken()


            else:
                self.__insertToken(TokenDict[self.equation[self.iterator]])
                self.iterator += 1

    def __ValAt(self):
        if self.iterator < len(self.equation):
            return self.equation[self.iterator]

    def __getNumberToken(self):
        number = ''
        while (self.__ValAt() in digs or self.__ValAt() == '.') and self.iterator < len(
                self.equation):
            number += self.__ValAt()
            self.iterator += 1

        self.__insertToken('NUM', float(number))

    def GetTokens(self):
        self.__getTokens()
        return self.tokens
