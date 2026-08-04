# Observer
class Observer:
    def update(self, shape):
        print(shape, "is drawn")

# Subject
class Shape:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def draw(self, shape):
        print("Drawing", shape)
        for observer in self.observers:
            observer.update(shape)

# Main
shape = Shape()
observer = Observer()

shape.attach(observer)

shape.draw("Circle")
shape.draw("Rectangle")