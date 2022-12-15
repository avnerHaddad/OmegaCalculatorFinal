from Config import*
class TokenNode:
    def __init__(self, val1, val2, type):
        self.val1 = val1
        self.val2 = val2
        self.type = type

    #func that executes the func for the corosponding operator type of the token using the dictonary
    def calc(self):
        try:
            return funcDict[self.type](self.val1, self.val2)
        except Exception as MathError:
            print(str(MathError))


