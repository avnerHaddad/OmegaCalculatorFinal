from Lexer import Lexer
from Mparser import Mparser
from Interpreter import Interpreter
from Config import *
from IOManager import *
import pytest

tests = {"1+2+3": 5, }


def calculatorUI():
    PrintTOConsole(welcomeMsgStr)
    while True:
        str = getInput()
        print("\n\n\n\n")
        Inter = Interpreter(str)
        try:
            answer = Inter.solve()
            print(answer)
        except MathException as mathException:
            print(mathException.__str__())


def calculatorNoCatch():
    str = getInput()
    Inter = Interpreter(str)
    answer = Inter.solve()
    print(answer)


calculatorUI()
# calculatorNoCatch()
