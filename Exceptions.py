class MathException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "unknown math exception occurred"


class divByZeroException(MathException):
    def __init__(self):
        pass

    def __str__(self):
        return "cant divide by zero..."


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


class InfinityException(MathException):
    def __init__(self):
        pass

    def __str__(self):
        return "number inside the equation reached infinity and thus can not be operated on in this calc"


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


class ComplexNumberException(MathException):
    def __init__(self):
        pass

    def __str__(self):
        return "result is a complex number and therefore could not be calculated"


class BigNumberException(MathException):
    def __init__(self):
        pass

    def __str__(self):
        return "number is too big and therefore, different math operations could not be available"


class notExpectedToParseException(MathException):
    def __init__(self, char, index, expected_to_parse):
        self.char = char
        self.index = index
        self.expected = expected_to_parse

    def __str__(self):
        return "the character: " + str(self.char) + \
               " can not be in the index:" + str(self.index) + "expected to parse one of the following:" + str(
            self.expected)


class UnusedOperatorException(MathException):
    def __init__(self):
        pass

    def __str__(self):
        return "operator missing an operand at the end of equation"
