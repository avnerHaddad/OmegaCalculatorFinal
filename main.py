from MathInterpreter import OmegaMathInterpreter
from Config import *
from IOManager import *


def calculatorUI():
    PrintTOConsole(welcomeMsgStr)
    MathInterpreter = OmegaMathInterpreter()
    while True:
        inputString = getInput()
        print("\n\n\n\n")
        try:
            answer = MathInterpreter.solve(inputString)
            print(answer)
        except MathException as mathException:
            print(mathException.__str__())


calculatorUI()
