# --------------------1---------------------------
from collections import defaultdict

text = "cat, dog, tac, god, act".split(', ')

result = defaultdict(set)

for word in text:
    sort_word = ''.join(sorted(word))
    result[sort_word].add(word)

print([list(v) for k, v in result.items() if len(v) > 1])


# ---------------------------2-------------------------------

def is_subset(set1, set2):
    temp1 = list(set1)
    temp2 = list(set2)
    tmp = 0

    if len(temp1) <= len(temp2):
        while tmp <= len(temp1) - 1:
            if temp1[tmp] in temp2:
                tmp += 1
            else:
                return False
        else:
            return True
    else:
        return False


print(is_subset({1, 2, 3}, {3, 1, 2, 4, 5}))
