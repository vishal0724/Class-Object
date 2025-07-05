class Item:
    # print("I am called!!")
    price_discount = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"price({price}) is not acceptable!!"
        assert quantity >= 0, f"quantity({quantity}) is not acceptable!!"

        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)


    """
    name as read only value, can't change..
    this is called ENCAPSULATION in opps.
    """
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, naam):
        return self.__name


    def __str__(self):
        return(self.__name)
    def __repr__(self):
        return (f"{self.__class__.__name__}({self.__name},{self.price}, {self.quantity})")

    @classmethod
    def about_class(cls):
        return "I am class methods."

    @staticmethod
    def stat(num):
        return num * 5, "I am static method."

    def total_price(self):
        return self.price * self.quantity
    def priceAfterDiscount(self):
        return self.price * self.price_discount

    """
    private methods(starting with '__') only used inside the class
    and can't access from outside
    This is called ABSTRACTION in opps
    """
    def __step1(self):
        return "step1 go"
    def __step2(self):
        return "step1 go"

    def sendPro(self):
        print(self.__step1())
        print(self.__step2())
        return "send process done"