# Parent Class
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Child Class
class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Child Class
class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Creating objects
d = Dog()
c = Cat()

d.sound()
c.sound()