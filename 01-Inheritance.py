"""
Instead of starting from scratch, you can create a class by deriving it from a pre-existing class.
Inheritance comes into picture when a new class possesses 'IS A' relationship with an existing class.
Car IS a vehicle. Bus IS a vehicle; Bike IS also a vehicle.
Vehicle here is the parent class, whereas car, bus and bike are the child classes.
"""


class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def divide(self):
        return self.a / self.b


class Modulus:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def mod_divide(self):
        return self.a % self.b


class DiVMod(Division, Modulus):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def div_and_mod(self):
        div_val = Division.divide(self)
        mod_val = Modulus.mod_divide(self)
        return (div_val, mod_val)


x = DiVMod(10, 3)
# can you notice that child class inherit parent methods
print(x.divide())
print(x.mod_divide())
print(x.div_and_mod())
