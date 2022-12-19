from Token import Token
from Config import *
from Exceptions import *


class Lexer:
    # lexer class for turning user input into identifiable token objects
    def __init__(self):
        self.tildaAvailable = True
        self.equation = None
        self.iterator = 0
        self.tokens = []
        # holds all the Types the lexer is predicting to lex next
        self.expectToParse = afterInfixAndPrefix
        # field that declares whether next minus should be unary
        self.insertUnary = True
        self.curChar = None

    # func that inserts a token to the list based on Type and value, inserts an unary minus if last parsed
    # requirements are met

    def isExpected(self, TYPE):
        if TYPE is 'TILDA' and not self.tildaAvailable:
            return False
        return self.contains(TYPE, self.expectToParse)

    # removes an item recursively from all subLists of a list
    def remove(self, Item, List):
        for lst in List:
            if type(List) == list:
                self.remove(Item, lst)
            else:
                if lst == Item:
                    List.remove(lst)

    # checks an item recursively from all subLists of a list if it exits inside
    def contains(self, Item, List):
        if type(List) == list:
            return any(self.contains(Item, l) for l in List)
        else:
            return Item == List

    # func that updates the ExpectToParse field based on what was just parsed
    def getExpectations(self, TYPE):
        # add orginised lists for them all?
        if TYPE is not 'TILDA':
            self.expectToParse = []
            if TYPE is 'NUM':
                self.expectToParse.append(afterNumAndPostFix)
                self.tildaAvailable = True
            elif TYPE in PostFixOps:
                self.expectToParse.append(afterNumAndPostFix)
            elif TYPE in infixOps:
                self.expectToParse.append(afterInfixAndPrefix)
            elif TYPE in preFixOps:
                self.expectToParse.append(afterInfixAndPrefix)
            elif TYPE in 'BRACKET_OPEN':
                self.expectToParse.append(afterInfixAndPrefix)
                self.tildaAvailable = True
            elif TYPE in 'BRACKET_CLOSE':
                self.expectToParse.append(afterBracketClose)

        else:
            self.tildaAvailable = False

    def __insertToken(self, TYPE, value=None):
        # inserts token to end of the token array while checking and updating expectations

        if TYPE is 'SUB' and self.insertUnary:
            TYPE = 'UNARY_MINUS'
        self.tokens.append(Token(TYPE, value))
        if not self.isExpected(TYPE):
            raise notExpectedToParseException(self.curChar, self.iterator, self.expectToParse)
        self.getExpectations(TYPE)

    # func that fills up the tokens list from the string the lexer is built of
    def __getTokens(self):
        # fills up the token array from the user input
        self.insertUnary = True
        while self.curChar is not None:
            if self.curChar in whitespace:
                self.Next()
            elif self.curChar in digs:
                self.__getNumberToken()
                self.insertUnary = False
            elif self.curChar in operators or self.curChar in bracketSymbols:
                self.__insertToken(TokenDict[self.equation[self.iterator]])
                if TokenDict[self.curChar] not in SingleDigOps and TokenDict[self.curChar] is not 'BRACKET_CLOSE':
                    self.insertUnary = True

                self.Next()
            else:
                raise InvalidCharException(self.curChar)

    # iterates over rest of the number and creates a number token, called when encountering a digit
    def __getNumberToken(self):
        number = ''
        dot_count = 0
        while (self.curChar in digs or self.curChar == '.') and self.iterator < len(
                self.equation):
            if self.curChar == '.':
                dot_count += 1
                if dot_count > 1:
                    raise Exception("duplicate decimal point")
            if self.curChar not in whitespace:
                number += self.curChar
            self.Next()
        number = float(number)
        number = round(number, 10)
        self.__insertToken('NUM', number)

    # public func that calls the internal get tokens and return the list generated
    def GetTokens(self, equation):
        # func to call externally, return an array of tokens from the input
        self.equation = equation
        self.curChar = self.equation[self.iterator]
        self.__getTokens()
        return self.tokens

    # moves the string index forward by 1
    def Next(self):
        # advance the iterator
        try:
            self.iterator += 1
            self.curChar = self.equation[self.iterator]
        except IndexError:
            self.curChar = None
