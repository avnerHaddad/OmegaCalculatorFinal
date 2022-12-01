from Lexer import Lexer
from Mparser import Mparser
str = input()
lexer = Lexer(str)
listOfTokens = (lexer.GetTokens())
for i in listOfTokens:
    print(i)
parser = Mparser(str)