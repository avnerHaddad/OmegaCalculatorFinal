from Lexer import Lexer
from Parser import Parser
str = input()
lexer = Lexer(str)
listOfTokens = (lexer.GetTokens())
for i in listOfTokens:
    print(i)
parser = Parser(str)