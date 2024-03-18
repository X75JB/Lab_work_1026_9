class CashRegister:
    def __init__(self):
        self._totalPrice = 0.0
        self._itemCount = 0

    def addItem(self, price):
        self._itemCount += 1
        self._totalPrice += price

    def clear(self):
        self._itemCount = 0
        self._totalPrice = 0.0

    def getTotal(self):
        return self._totalPrice