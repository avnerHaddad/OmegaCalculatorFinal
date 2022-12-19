from Exceptions import*

#to add a new operator, add the func for it, fill it in the operators and dicts for its requiremnts untill you reach constants

#functions for operators and helper funcs
def isArealFloat(num):
    if(type(num) == float):
        float_str = str(num)
        if (float_str.split('.')[1] != '0' and len(float_str[1]) > 1):
            return True
    return False
def num(num1,num2):
    return num1
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    if num2 is not None:
        return  num1-num2
    else:
        return -num1
def mul(num1,num2):
    return(num1*num2)
def div(num1,num2):
    if(num2 is not 0):
        ans = num1/num2
        if ans == float("inf"):
            raise InfinityException
        return(num1/num2)
    raise divByZeroException
def power(num1,num2):
    try:
        ans = pow(num1,num2)
        if type(ans) is complex:
            raise ComplexNumberException
        return ans
    except OverflowError:
        raise InfinityException


    return
def mod(num1,num2):
    if(num2 == 0):
        raise ModByZeroException
    return(num1%num2)
def max(num1,num2):
    if(num1 > num2):
        return num1
    return num2
def min(num1,num2):
    if(num1 < num2):
        return num1
    return num2
def avg(num1,num2):
    return((num1+num2)/2)
def neg(num1,num2):
    return -num1
def factorial(num1,num2):
    if num1 > 200:
        raise InfinityException
    if(num1 < 0):
        raise NegativeFactorialException
    if(not isArealFloat(num1)):
        num = 1
        num = float(num)
        for i in range(1, int(num1)+1):
            num = num * i
            if(num == float("inf")):
                return float("inf")
        return num
    raise FloatFactorialException
def dig_sum(num1,num2):
    sign = 1
    if(num1 < 0):
        sign = -1
        num1 = num1*sign
    digsum = 0
    while num1 > 0:
        digsum += int(num1%10)
        num1 = int(num1/10)
    return digsum * sign
TokenTypes = ['NUM', 'ADD', 'SUB', 'MUL', 'DIV', 'POW', 'MOD', 'MAX', 'MIN', 'AVG', 'TILDA', 'FACTORIAL', 'BRACKET_OPEN','BRACKET_CLOSE', 'DIG_SUM', 'UNARY_MINUS']
operators = ['+', '-', '*','/', '^', '%', '$', '&', '@', '~', '!','#']
TokenDict = {'+': 'ADD', '-':'SUB', '*':'MUL','/':'DIV', '^':'POW', '%':'MOD', '$' : 'MAX', '&' : 'MIN', '@' : 'AVG', '~' : 'TILDA', '!' : 'FACTORIAL', '(': 'BRACKET_OPEN', ')':'BRACKET_CLOSE', '#' : 'DIG_SUM'}
TokenPowerDict = {'NUM':999, 'ADD':1, 'SUB':1, 'MUL':2, 'DIV':2, 'POW':3, 'MOD':3, 'MAX':4, 'MIN':4, 'AVG':4, 'TILDA':6, 'FACTORIAL':6, 'BRACKET_OPEN':0,'BRACKET_CLOSE':0, 'DIG_SUM':6, 'UNARY_MINUS':999}
SingleDigOps = ['UNARY_MINUS', 'TILDA', 'FACTORIAL','DIG_SUM']
PostFixOps = ['FACTORIAL','DIG_SUM']
infixOps = ['ADD', 'SUB', 'MUL', 'DIV', 'POW', 'MOD', 'MAX', 'MIN', 'AVG']
preFixOps = ['UNARY_MINUS','TILDA']

funcDict = {'NUM': num,'ADD': add, 'SUB': sub, 'MUL': mul,'DIV': div,"POW": power,"MOD": mod,"MAX":max,"MIN":min,"AVG":avg,"TILDA":neg, "FACTORIAL":factorial, "DIG_SUM": dig_sum, "UNARY_MINUS":neg}
level1 = ['SUB', 'ADD']
level2 = ['MUL', 'DIV']
level3 = ['POW']
level4 = ['MOD']
level5 = ['MAX','MIN','AVG']
level7 = ['NUM']
level6 = ['TILDA']
levelDict = {1:level1, 2:level2, 3:level3, 4:level4, 5:level5, 6:level6, 7:level7}
finalLevel = len(levelDict)
#------------------------------------------------------------------------------------------------

#from here on these are CONSTANTS do not touh unless you know what you are doing!
bracketSymbols = [')','(']
brackets = ['BRACKET_OPEN','BRACKET_CLOSE']
whitespace = ['\t',' ','\r']
digs = ['0','1','2','3','4','5','6','7','8','9', ' ']
welcomeMsgStr = "hello and welcome to the omega calculator, feel free to use these operators to calculate stuff:\n" + str(TokenDict)





#expect to parse after: nums and PostFixOps
#includes, postfixOps, infixOps,BracketClose
afterNumAndPostFix = []
afterNumAndPostFix.append('BRACKET_CLOSE')
afterNumAndPostFix.append(infixOps)
afterNumAndPostFix.append(PostFixOps)
#after after infix,prefix,openBraacket
#includes, nums, prefix ops, and bracket open
afterInfixAndPrefix = []
afterInfixAndPrefix.append('NUM')
afterInfixAndPrefix.append('BRACKET_OPEN')
afterInfixAndPrefix.append(preFixOps)
#after after Breacket
#includes bracket close, infix ops and postFixOps
afterBracketClose = []
afterBracketClose.append('BRACKET_CLOSE')
afterBracketClose.append(PostFixOps)
afterBracketClose.append(infixOps)







