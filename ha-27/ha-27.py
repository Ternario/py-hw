# ---------------- Task 1 ---------------------

from functools import reduce


def sum_sqrt_numbers(num_list: list) -> int:
    # return reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, num_list)))
    return reduce(lambda x, y: x + y ** 2, filter(lambda x: x % 2 == 0, num_list), 0)


print(sum_sqrt_numbers([int(num) for num in input("Enter list of numbers: ").split(",")]))

# ---------------- Task 2 ---------------------


def compose_functions(func_arr: list, num: int) -> int:
    temp = num

    for i in func_arr:
        temp = i(temp)

    return temp


def add_one(n):
    return n + 1


def double(n):
    return n * 2


def subtract_three(n):
    return n - 3


print(compose_functions([add_one, double, subtract_three], 5))
