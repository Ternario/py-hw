# ---------------------------- Task 1 --------------------------------
from typing import List, Tuple


def find_longest_word(word_arr: List[str]) -> str:
    return max(word_arr, key=len)


words = ["apple", "banana", "cherry", "dragonfruit"]
result = find_longest_word(words)
print(result)


# ---------------------------- Task 2 --------------------------------

def calculate_total_price(products_arr: list[Tuple[str, float, int]]) -> float:
    price_sum = 0
    for i in products_arr:
        price_sum += i[1]
    return price_sum


with open("products.txt", "r", encoding="utf-8") as file:
    file = [i.split(",") for i in file.readlines()]
    new_file_arr = [(i[0], float(i[1]), int(i[2])) for i in file]

    print(calculate_total_price(new_file_arr))
