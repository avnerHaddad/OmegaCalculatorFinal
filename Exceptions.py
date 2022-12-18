
class MathException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "unknown math exception occurred"


class TildaException(MathException):
    def __init__(self):
        pass

    def __str__(self):
        return "tilda can not be used as an operator use '-' instead"


class InvalidCharException(MathException):
    def __init__(self, char):
        self.char = char

    def __str__(self):
        return str(self.char) + " is not supported by this calculator"


class NegativeFactorialException(MathException):
    def __init__(self):
        pass

    def __str__(self):
        return "factorial can not be done on a negative number"


class FloatFactorialException(MathException):
    def __init__(self):
        pass

    def __str__(self):
        return "factorial can not be done on a float number, num must be an integer"


class DoubleTildaExcecption(MathException):
    def __init__(self):
        pass

    def __str__(self):
        return "Tilda can only be used once on each number, consider using a '-' "

class EmptyInputException(MathException):
    def __init__(self, char):
        pass

    def __str__(self):
        return "please input something into the calculator, input must not be empty"

class UnclosedBracketException(MathException):
    def __init__(self):
        pass

    def __str__(self):
        return "all open brackets need to be closed off"

class PostFixOperatorOutOfPlaceException(MathException):
    def __init__(self):
        pass

    def __str__(self):
        return "Post fix operators must be after the number they are operated on(!,#...)"

class ModByZeroException(MathException):
    def __init__(self):
        pass

    def __str__(self):
        return "can not do module with 0 "

class DoubleOperatorException(MathException):
    def __init__(self):
        pass

    def __str__(self):
        return "can not place 2 double operand operators one after another"

class UnusedOperatorException(MathException):
    def __init__(self):
        pass

    def __str__(self):
        return "left an operator with no number to operate on in the string"


class ComplexNumberException(MathException):
    def __init__(self):
        pass

    def __str__(self):
        return "result is a complex number and therefore could not be calculated"


class SolamitException(MathException):
    def __init__(self):
        pass

    def __str__(self):
        return "number is too big to use # on and is represented with E"

class notExpectedToParseException(MathException):
    def __init__(self,char, index,expectedToParse):
        self.char = char
        self.index = index
        self.expected = expectedToParse

    def __str__(self):
        return "the character: " + str(self.char) + \
               " can not be in the index:" + str(self.index) + "expected to parse one of the following:" +  str(self.expected)
