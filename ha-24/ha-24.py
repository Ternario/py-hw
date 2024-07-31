# ---------------------------- Task 1 --------------------------------

def counter_func():
    cur_sum = 0

    while True:
        next_sum = yield cur_sum
        if next_sum:
            cur_sum += next_sum
            print(f"current amount: {cur_sum}")


amount = counter_func()
next(amount)

while True:
    number = int(input("Enter a number: "))

    if number != 0:
        amount.send(number)
    else:
        print(f"current amount: {next(amount)}")
        break


# ---------------------------- Task 2 --------------------------------

def arifmetic_func(a, b, c):
    count = a
    while count < b:
        yield count
        count += c


for i in arifmetic_func(1, 10, 2):
    print(i)
