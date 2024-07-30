# ---------------------------- Task 1 --------------------------------
def generate_squares(num):
    return [n ** 2 for n in range(1, num + 1)]


for i in generate_squares(int(input("Enter the number: "))):
    print(i)


# ---------------------------- Task 2 --------------------------------
def fib_func():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


fib_func_gen = fib_func()

for i in range(int(input("Enter the number: "))):
    print(next(fib_func_gen))
