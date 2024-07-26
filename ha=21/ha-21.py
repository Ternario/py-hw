# --------------------- Task 1 ------------------
from re import sub
from collections import Counter


def count_words(text):
    result = Counter()

    new_list = sub(r"\W", " ", text.lower()).split()

    for i in new_list:
        result[i] += 1

    return result


new_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est"

print({k: v for k, v in count_words(new_text).items() if v > 1})

# --------------------- Task 2 ------------------

from collections import namedtuple

date = [
    ("Alice", 25, "New York"),
    ("Bob", 30, "London"),
    ("Carol", 35, "Paris"),
]

Person = namedtuple("Person", ["name", "age", "city"])
list_of_persons = [Person(*arg) for arg in date]

for item in list_of_persons:
    print(f"Name: {item.name}, Age: {item.age}, City: {item.city}")


# --------------------- Task 3 ------------------

def get_value_from_dict(dict, value, met):
    if met == "y":
        return dict.get(value)
    else:
        return dict.setdefault(value)


my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}

key = input("Enter the key for search: ")
method = input("Use method get (y/n): ").lower()

print(f"Key value: {get_value_from_dict(my_dict, key, method)}")
