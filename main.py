from Lexer import Lexer

lexer = Lexer(input())
listOfTokens = (lexer.GetTokens())
for i in listOfTokens:
    print(i)