from Config import TokenTypes
class Token():
    def __init__(self, type, value):
        if(type in TokenTypes):
            self.type = type
            self.value = value
        else:
            return
            #add an exception later
        