from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Circle Class
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

# Rectangle Class
class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

# Factory Class
class ShapeFactory:
    def create_shape(self, choice):
        if choice == 1:
            r = float(input("Enter radius: "))
            return Circle(r)
        elif choice == 2:
            l = float(input("Enter length: "))
            b = float(input("Enter breadth: "))
            return Rectangle(l, b)
        else:
            return None

# Main
factory = ShapeFactory()

print("1. Circle")
print("2. Rectangle")
choice = int(input("Enter your choice: "))

shape = factory.create_shape(choice)

if shape:
    print("Area =", shape.area())
else:
    print("Invalid Choice")