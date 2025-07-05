from item import Item

class Phone(Item):
    def __init__(self, name, price, quantity= 0, brokenPhone = 0):
        super().__init__(name, price, quantity)
        assert brokenPhone >= 0, f"brokenPhone({brokenPhone}) is not acceptable!!"
        self.brokenPhone = brokenPhone