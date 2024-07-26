# ------------------- Task 1 -----------------------
def merge_dicts(**kwargs):
    result = {}

    for i in kwargs.values():
        for k, v in i.items():
            if k in result:
                result[k].append(v)
            else:
                result[k] = [v]

    return result


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'c': 5, 'd': 6}

print(merge_dicts(dict1=dict1, dict2=dict2, dict3=dict3))


# ------------------- Task 2 -----------------------

def count_unique_chars(text):
    return len(set(text))


print(count_unique_chars("hello"))


# ------------------- Task 3 -----------------------

def calculate_average_grade(dict_arg):
    new_dict = {}

    for k, v in dict_arg.items():
        new_dict[k] = sum(v) / len(v)

    return new_dict


grades = {'Alice': [85, 90, 92], 'Bob': [78, 80, 84], 'Carol': [92, 88, 95]}

print(calculate_average_grade(grades))
