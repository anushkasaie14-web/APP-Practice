class Engine:
    def start(self):
        print("Engine starts")


class Car:
    def __init__(self):
        self.engine = Engine()   # Composition

    def drive(self):
        self.engine.start()
        print("Car is running")


car = Car()
car.drive()