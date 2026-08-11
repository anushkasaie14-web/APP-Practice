class Numbers:
    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <= 3:
            x = self.n
            self.n += 1
            return x
        raise StopIteration


obj = Numbers()

for x in obj:
    print(x)