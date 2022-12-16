from Lexer import Lexer
from Mparser import Mparser
from Interpreter import Interpreter
from Config import *
from IOManager import *

def calculatorUI():
        PrintTOConsole(welcomeMsgStr)
        while True:
                str = getInput()
                print("\n\n\n\n")
                Inter = Interpreter(str)
                Inter.solve()
calculatorUI()






