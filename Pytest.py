import pytest

from Interpreter import Interpreter
from Exceptions import *


def calc(inputStr):
    Inter = Interpreter(inputStr)
    answer = Inter.solve()
    return answer


# Simple syntax errors
def test_missing_operator():
    # missing operator between the 3 and the (34-20)
    inputEquation = "3(34-20)"
    with pytest.raises(notExpectedToParseException):
        calc(inputEquation)


def test_Unclosed_Bracket():
    # missing closing paren
    inputEquation = "((10-23)+3!"
    with pytest.raises(UnclosedBracketException):
        calc(inputEquation)


# Nonsense inputEquations
def test_invalidChars():
    # = is an invalid character
    inputEquation = "a+5d"
    with pytest.raises(InvalidCharException):
        calc(inputEquation)


# Empty inputEquation
def test_empty_inputEquation():
    # an empty inputEquation
    inputEquation = " "
    with pytest.raises(EmptyInputException):
        calc(inputEquation)


def test_double_tilda():
    inputEquation = "5~-~3"
    with pytest.raises(UnusedOperatorException):
        calc(inputEquation)


def test_double_tilda2():
    inputEquation = "~-~3"
    with pytest.raises(InvalidCharException):
        calc(inputEquation)


# Whitespaced characters
def test_whitespace_inputEquation():
    # a inputEquation that contains whitespaces only
    inputEquation = "   \t\r"
    with pytest.raises(EmptyInputException):
        calc(inputEquation)


# correct
# Valid complex equations
def eq01():
    # (18)
    inputEquation = "(3*(5-2)!)/((5!)/((-2^2)!)+1)"
    assert int(calc(inputEquation)) == 3


# correct
def eq02():
    inputEquation = "((5&2)^(2^2$-4)- 3!)*-(-2@5!#!)"
    assert calc(inputEquation) == -20


# correct
def eq03():
    inputEquation = "4!#^ 2 -(2^(-(2^2)@(2^3)))!"
    assert calc(inputEquation) == 12


# correct
def eq04():
    inputEquation = "((22/2)^2)#! - ~---120#!"
    assert calc(inputEquation) == 18


# correct
def eq05():
    inputEquation = "(10*(5@15))@((15%4)^(2^2))"
    assert calc(inputEquation) == 90.5


# correct
def eq06():
    inputEquation = "((7!/6!)^2+1)- (40@((4*5)$60))"
    assert calc(inputEquation) == 0


# correct
def eq07():
    inputEquation = "(19%(4!/4)+2)^(~---2! + 2^3 - (4^2)/2)"
    assert calc(inputEquation) == 9


# correct
def eq08():
    inputEquation = "((7 *(2^2))/2)@(5*(((3^2)*2)/6))"
    assert calc(inputEquation) == 14.5


# corret
def eq09():
    inputEquation = "((7*3+2)#^-(-2&5)*2)*(5*2-4!#)"
    assert calc(inputEquation) == 200


def eq10():
    inputEquation = "((2*2*2)*3!)-(((20^2)/2)/20)*6"
    assert calc(inputEquation) == -12


def eq11():
    inputEquation = "(4!/2^3)^2+2^((20+6@(2^3))/3^2)"
    assert calc(inputEquation) == 17


def eq12():
    inputEquation = "(6*3+1@(6^2/(2^2*3)))/(6!#-(8*5+1)#)"
    assert calc(inputEquation) == 5


def eq13():
    inputEquation = "(11^2)%((10+1!#)*((5*2^1)&(5*2^2)))"
    assert calc(inputEquation) == 11


def eq14():
    inputEquation = "42%(6!#-(2^2*2^3+10)%(2^3+5&12))"
    assert calc(inputEquation) == 0


def eq15():
    inputEquation = "-(2^3)*(5!#+3)+((5^2*2^2)/10+~---4)"
    assert calc(inputEquation) == -34


def eq16():
    inputEquation = "-((5+5+150%(40*3))*2@3)-(7*2^(11%(2^1*2^2)))"
    assert calc(inputEquation) == -156


def eq17():
    inputEquation = "-((6$4*3)*2^-2+(25%(3*596)))+(20-(2^2)@(2*3)-2)"
    assert calc(inputEquation) == -16.5


def eq18():
    inputEquation = "(30$14)*120#+2^(2&10)-(0.5+1/(16%((5!+1)/11)))"
    assert calc(inputEquation) == 93.3


def eq19():
    inputEquation = "50*(0.04*10^2)+3-2^(~--5@(10+(10*10)#))"
    assert calc(inputEquation) == 195


def eqq20():
    inputEquation = "((10+10+10+3^2)/5!#)^2-(0.5*(2^-(-2&2)))"
    assert calc(inputEquation) == 167
