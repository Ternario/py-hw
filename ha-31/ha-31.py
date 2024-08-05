# ---------------- Task 1 ---------------------

def validate_args(*decor_arg):
    def passed_func(func):
        def wrapper(*func_args):
            for i in range(len(decor_arg)):
                if not isinstance(func_args[i], decor_arg[i]):
                    raise TypeError(
                        f"Arg [{i}]={func_args[i]} has wrong type {type(func_args[i])}. Expected: {decor_arg[i]}")
            func(*func_args)

        return wrapper

    return passed_func


@validate_args(int, str)
def greet_func(age, name):
    print(f"Hello {name}! You are {age} ears old.")


greet_func(27, "Andrii")
greet_func("27", "Andrii")

# ---------------- Task 2 ---------------------

import logging

logging.basicConfig(level=logging.INFO, filename="log.txt", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


def log_args(func):
    def wrapper(*args):
        res = func(*args)
        logging.info(f"Arguments: {args}, Result: {res}")

    return wrapper


@log_args
def add_num(a, b):
    return a + b


add_num(2, 3)
add_num(5, 7)
