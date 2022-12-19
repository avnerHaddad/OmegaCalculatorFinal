import sys

from Exceptions import*
def PrintTOConsole(str):

    print(str)

def getInput():
    try:
        print("\nenter your calculation:\n")
        userinput = input(">>")
        return userinput
    except EOFError:
        print("you pressed EOF and program must close")
        exit(1)
    except EmptyInputException:
        print("you can not use an empty input, enter something")
    except KeyboardInterrupt:
        print("exiting the calculator")
        exit(1)

