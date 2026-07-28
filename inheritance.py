# Parent Class
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Child Class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Creating object
d = Dog()

d.sound()   # Inherited method
d.bark()    # Child class method