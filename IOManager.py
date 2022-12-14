
def PrintTOConsole(str):
    print(str)

def getInput(message):
    Userinput = input(str)
    if(Userinput == ' '):
        raise Exception(EMPTYINPUT)