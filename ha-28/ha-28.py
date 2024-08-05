# ---------------- Task 1 ---------------------

def comprehension_func(word_list: list, vovwl_letters: str) -> list:
    return list(map(lambda x: x.upper(), [word for word in word_list if word[0].lower() in vovwl_letters]))


vovwel_str = "aoueiy"
words_str = "order, Map, cat, eagle, boat, Ananas, issue, Underground, Tooth, poker"

print(comprehension_func(words_str.split(", "), vovwel_str))

# ---------------- Task 2 ---------------------

from functools import reduce
from itertools import accumulate
from operator import mul


def sum_count(numbers_list: list) -> str:
    num_sum = reduce(lambda x, y: x * y, numbers_list)
    iter_sum = accumulate(numbers_list, mul)

    return f"{num_sum}\n{list(iter_sum)}"


print(sum_count([int(num) for num in input("Enter list of numbers: ").split()]))
