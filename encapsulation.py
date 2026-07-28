# Encapsulation Example

class Student:
    def __init__(self):
        self.__name = ""
        self.__age = 0

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age > 0:
            self.__age = age

    # Getter methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


# Creating object
s = Student()

# Setting values
s.set_name("AAnushka")
s.set_age(20)

# Getting values
print("Name:", s.get_name())
print("Age:", s.get_age())