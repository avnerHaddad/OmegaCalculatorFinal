from Config import TokenDict, numbers
import Token
class Lexer:
    def __init__(self, input):
        self.input = input
        self.index = 0
        self.tokens = []


    def __insertToken(self,TYPE, value = None):
        self.tokens.append(Token(TYPE, value))

    def __getTokens(self):
        while self.index < len(self.input):
            if self.__ValAt(self, self.index) in numbers:
                self.__getNumberToken()
                self.index += 1


            else:
                self.__insertToken(self, TokenDict(self.input(self.index)))
                self.index += 1



    def __ValAt(self, index):
        return self.input(self.index)
    def __getNumberToken(self):
        number  = ''
        while (self.__ValAt(self, self.index) in numbers or self.__ValAt(self, self.index) == '.') and self.index >= len(self.input):
            number += self.__ValAt(self, self.index)
            self.index += 1

        self.__insertToken(self, 'NUM', float(number))



    def GetTokens(self):
        self.__getTokens()
        return self.tokens



