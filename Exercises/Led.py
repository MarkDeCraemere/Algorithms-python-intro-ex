class Led:
    def __init__(self):
        self.__LedStates = 0

    def GetLedBin(self):
        return bin(self.__LedStates)

    def GetLedDecimal(self):
        return self.__LedStates

    def GetLedHex(self):
        return hex(self.__LedStates)

    def Increment(self):
        if self.__LedStates < 16:
            self.__LedStates += 1

    def Decrement(self):
        if self.__LedStates > 0:
            self.__LedStates -= 1