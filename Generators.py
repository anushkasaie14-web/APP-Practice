def my_generator():
    for i in range(1, 6):
        yield i

for value in my_generator():
    print(value)