from Config import TokenTypes


class Token():
    def __init__(self, type, value):
        if (type in TokenTypes):
            self.type = type
            self.value = value
        else:
            self.type = 'error'
            self.value = 0
            # add an exception later

    def __str__(self):
        return "type: " + self.type + " val:" + str(self.value)
