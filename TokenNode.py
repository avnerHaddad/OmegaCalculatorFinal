
class TokenNode:
    def __init__(self,token1,token2, type):
        self.val1 = token1
        self.val2 = token2
        self.type = type

def calc(self):
    return funcDict[type](self.val1, self.val2)

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return  num1-num2
def mul(num1,num2):
    return(num1*num2)
def div(num1,num2):
    return(num1/num2)

def power(num1,num2):
    return pow(num1,num2)

def mod(num1,num2):
    return(num1-(num1/num2)*num2)

def max(num1,num2):
    if(num1 > num2):
        return num1
    return num2

def min(num1,num2):
    if(num1 < num2):
        return num1
    return num2
def avg(num1,num2):
    return(num1+num2/2)

def neg(num1):
    return -num1

def factorial(num1):
    if num1 == 0:
        #exit case
        return 1
    else:
        #multiply by the prev num
        return num1 * factorial(num1 - 1)


funcDict = {"+": add, "-": sub, "*": mul,"/": div,"^": power,"%": mod,"$":max,"&":min,"@":avg,"~":neg, "!":factorial }