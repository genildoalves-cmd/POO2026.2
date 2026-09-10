class Banco:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def __eq__(self, other) -> bool:
        if isinstance(other, Banco):
            return self.number1 == other.number1 and self.number2 == other.number2


a = Banco("123", "456")
b = Banco("123", "456")


print(a == b)  # true
print(a in [b])  # true)
