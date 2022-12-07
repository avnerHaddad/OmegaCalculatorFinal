from Config import TokenDict, digs, operators
from Token import Token


class Lexer:
    # lexer class for turning user input into identifiable tokens
    def __init__(self, equation):
        self.equation = equation
        self.iterator = 0
        self.tokens = []

    def __insertToken(self, TYPE, value=None):
        # inserts token to end of the token array
        self.tokens.append(Token(TYPE, value))

    def __getTokens(self):
        # fills up the token array from the user input
        while self.iterator < len(self.equation):
            if self.__curChar() == ' ':
                self.Next()
            elif self.__curChar() in digs:
                self.__getNumberToken()
            elif self.__curChar() in operators:
                self.__insertToken(TokenDict[self.equation[self.iterator]])
                self.Next()
            else:
                raise Exception("char" + self.__curChar() + " is not a part of the calc")

    def __curChar(self):
        # return the value/char the iterator is currently at
        if self.iterator < len(self.equation):
            return self.equation[self.iterator]

    def __getNumberToken(self):
        # iterates over rest of the number and creates a number token, called when encountering a digit

        number = ''
        dotCount = 0
        while (self.__curChar() in digs or self.__curChar() == '.') and self.iterator < len(
                self.equation):
            if(self.__curChar() == '.'):
                dotCount += 1
                if(dotCount > 1):
                    raise Exception("duplicate decimal point")
            if self.__curChar() != ' ':
                number += self.__curChar()
            self.Next()

        self.__insertToken('NUM', float(number))

    def GetTokens(self):
        # func to call externally, return an array of tokens from the input
        self.__getTokens()
        return self.tokens

    def Next(self):
        # advance the iterator
        self.iterator += 1