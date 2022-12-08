from Lexer import Lexer
from Mparser import Mparser
from Interpreter import Interpreter
from Config import *
str = input()

"""
lexer = Lexer(str)
listOfTokens = (lexer.GetTokens())
for i in listOfTokens:
    print(i)
parser = Mparser(str)
parser.PrintParsed()
"""

print("\n\n\n\n")
Inter = Interpreter(str)
print(Inter.solve())



