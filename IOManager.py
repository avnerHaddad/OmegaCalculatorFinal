import sys

from Exceptions import*
def PrintTOConsole(str):

    print(str)

def getInput():
    try:

        print("\nenter your calculation:\n")
        userinput = input(">>")
        if not userinput.isspace() and userinput is not '':
            return userinput
        else:
            print("string is empty")
            raise EmptyInputException
    except EOFError:
        print("end of file error occurred, try again")
    except EmptyInputException:
        print("you can not use an empty input, enter something")
    except KeyboardInterrupt:
        print("exsiting the calculator")
        sys.exit(1)

