



class TildaException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "tilda can not be used as an operator use '-' instead"


class InvalidCharException(Exception):
    def __init__(self, char):
        self.char = char

    def __str__(self):
        return self.char + "is not supported by this calculator"


class NegativeFactorialException(Exception):
    def __init__(self, char):
        pass

    def __str__(self):
        return "factorial can not be done on a negative number"


class FloatFactorialException(Exception):
    def __init__(self, char):
        pass

    def __str__(self):
        return "factorial can not be done on a float number, num must be an integer"


class DoubleTildaExcecption(Exception):
    def __init__(self, char):
        pass

    def __str__(self):
        return "Tilda can only be used once on each number, consider using a '-' "

class EmptyInputException(Exception):
    def __init__(self, char):
        pass

    def __str__(self):
        return "please input something into the calculator, input must not be empty"

class UnclosedBracketException(Exception):
    def __init__(self, char):
        pass

    def __str__(self):
        return "all open brackets need to be closed off"

class PostFixOperatorOutOfPlaceException(Exception):
    def __init__(self, char):
        pass

    def __str__(self):
        return "Post fix operators must be after the number they are operated on(!,#...)"

class ModByZeroException(Exception):
    def __init__(self, char):
        pass

    def __str__(self):
        return "can not do module with 0 "

class DoubleOperatorException(Exception):
    def __init__(self, char):
        pass

    def __str__(self):
        return "can not place 2 double operand operators one after another"

class UnusedOperatorException(Exception):
    def __init__(self, char):
        pass

    def __str__(self):
        return "left an operator with no number to operate on in the string"


