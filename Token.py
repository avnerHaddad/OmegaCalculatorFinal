class Token():
    def __init__(self, type, value):
            self.type = type
            self.value = value

    def __str__(self):
        return "type: " + self.type + " val:" + str(self.value)
