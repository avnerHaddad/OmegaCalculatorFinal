from Lexer import Lexer
class Parser:

    def __int__(self, input):
        self.lexer = Lexer(input)
        self.index = 0
        self.tokens = self.lexer.GetTokens()

    def Parse(self):
        pass

    def __Next(self):
        self.index += 1

    def __curVal(self):
        self.tokens[self.index]



