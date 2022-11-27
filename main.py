from Lexer import Lexer

lexer = Lexer('!5+3*2')
listOfTokens = (lexer.GetTokens())
for i in listOfTokens:
    print(i)