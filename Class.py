class Item:
    # print("I am called!!")
    price_discount = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"price({price}) is not acceptable!!"
        assert quantity >= 0, f"quantity({quantity}) is not acceptable!!"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __str__(self):
        return(self.name)
    def __repr__(self):
        return (f"Item ({self.name},{self.price}, {self.quantity})")

    def total_price(self):
        return self.price * self.quantity
    def priceAfterDiscount(self):
        return self.price * self.price_discount

i1 = Item('Phone', 1000, 4)
i2 = Item('Laptop', 10000, 2)

print(Item.all)
print(i1.all)
