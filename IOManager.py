from Exceptions import*
def PrintTOConsole(str):

    print(str)

def getInput(message):
    try:
        Userinput = input(str)
        if(Userinput == ' '):
            raise Exception(EmptyInputException)
    except EOFError:
        pass
    except EmptyInputException:
        pass
    except KeyboardInterrupt:
        pass
