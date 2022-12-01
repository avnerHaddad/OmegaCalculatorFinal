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


    def __level1(self):
        pass

    def __level2(self):
        pass
    def __level3(self):
        pass
    def __level4(self):
        pass
    def __level5(self):
        pass
    def __level6(self):
        pass
