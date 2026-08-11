class CreditCard:
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI")


class Payment:
    def __init__(self, method):
        self.method = method

    def make_payment(self, amount):
        self.method.pay(amount)


p1 = Payment(UPI())
p1.make_payment(500)

p2 = Payment(CreditCard())
p2.make_payment(1000)