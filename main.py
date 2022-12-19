from Interpreter import Interpreter
from Config import *
from IOManager import *


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


def main(args):
    calculatorUI()
