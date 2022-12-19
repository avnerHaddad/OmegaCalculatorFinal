import pytest

from MathInterpreter import OmegaMathInterpreter
from Exceptions import *


def calc(inputStr):
    MathInterpreter = OmegaMathInterpreter()
    inputString = inputStr
    print("\n\n\n\n")
    answer = MathInterpreter.solve(inputString)
    return answer


# Simple syntax errors
def test_missing_operator():
    # missing operator between the 3 and the (34-20)
    testInput = "3(34-20)"
    with pytest.raises(notExpectedToParseException):
        calc(testInput)


def test_Unclosed_Bracket():
    # missing closing paren
    testInput = "((10-23)+3!"
    with pytest.raises(UnclosedBracketException):
        calc(testInput)


# Nonsense testInputs
def test_invalidChars():
    # = is an invalid character
    testInput = "a+5d"
    with pytest.raises(InvalidCharException):
        calc(testInput)


# Empty testInput
def test_empty_testInput():
    # an empty testInput
    testInput = " "
    with pytest.raises(EmptyInputException):
        calc(testInput)


def test_double_tilda():
    testInput = "5~-~3"
    with pytest.raises(notExpectedToParseException):
        calc(testInput)


def test_double_tilda2():
    testInput = "~-~3"
    with pytest.raises(notExpectedToParseException):
        calc(testInput)


# Whitespaced characters
def test_whitespace_testInput():
    # a testInput that contains whitespaces only
    testInput = "\t\r"
    with pytest.raises(EmptyInputException):
        calc(testInput)


# correct
# Valid complex testuations
def test01():
    # (18)
    testInput = "(3*(5-2)!)/((5!)/((-2^2)!)+1)"
    assert int(calc(testInput)) == 3


# correct
def test02():
    testInput = "((5&2)^(2^2$-4)- 3!)*-(-2@5!#!)"
    assert calc(testInput) == -20


# correct
def test03():
    testInput = "4!#^ 2 -(2^(-(2^2)@(2^3)))!"
    assert calc(testInput) == 12



def test04():
    testInput = "((22/2)^2)#! - ~---120#!"
    assert calc(testInput) == 18


def test05():
    testInput = "(10*(5@15))@((15%4)^(2^2))"
    assert calc(testInput) == 90.5


def test06():
    testInput = "((7!/6!)^2+1)- (40@((4*5)$60))"
    assert calc(testInput) == 0


def test07():
    testInput = "(19%(4!/4)+2)^(~---2! + 2^3 - (4^2)/2)"
    assert calc(testInput) == 9


def test08():
    testInput = "((7 *(2^2))/2)@(5*(((3^2)*2)/6))"
    assert calc(testInput) == 14.5


def test09():
    testInput = "((7*3+2)#^-(-2&5)*2)*(5*2-4!#)"
    assert calc(testInput) == 200


def test10():
    testInput = "((2*2*2)*3!)-(((20^2)/2)/20)*6"
    assert calc(testInput) == -12


def test11():
    testInput = "(4!/2^3)^2+2^((20+6@(2^3))/3^2)"
    assert calc(testInput) == 17


def test12():
    testInput = "(6*3+1@(6^2/(2^2*3)))/(6!#-(8*5+1)#)"
    assert calc(testInput) == 5


def test13():
    testInput = "(11^2)%((10+1!#)*((5*2^1)&(5*2^2)))"
    assert calc(testInput) == 11


def test14():
    testInput = "42%(6!#-(2^2*2^3+10)%(2^3+5&12))"
    assert calc(testInput) == 0


def test15():
    testInput = "-(2^3)*(5!#+3)+((5^2*2^2)/10+~---4)"
    assert calc(testInput) == -34


def test16():
    testInput = "-((5+5+150%(40*3))*2@3)-(7*2^(11%(2^1*2^2)))"
    assert calc(testInput) == -156


def test17():
    testInput = "-((6$4*3)*2^-2+(25%(3*596)))+(20-(2^2)@(2*3)-2)"
    assert calc(testInput) == -16.5


def test18():
    testInput = "(30$14)*120#+2^(2&10)-(0.5+1/(16%((5!+1)/11)))"
    assert calc(testInput) == 93.3


def test19():
    testInput = "50*(0.04*10^2)+3-2^(~--5@(10+(10*10)#))"
    assert calc(testInput) == 195


def testq20():
    testInput = "((10+10+10+3^2)/5!#)^2-(0.5*(2^-(-2&2)))"
    assert calc(testInput) == 167
