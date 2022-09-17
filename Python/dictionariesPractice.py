# REVERSE A DICT

# unique value, with dict comprehension
my_dict = {"A": 1, "B": 2, "C": 3, "D": 4}
inv_dict = {v: k for k, v in my_dict.items()}
print(inv_dict)

# not unique value
my_dict2 = {"A": 1, "B": 2, "C": 3, "D": 1}
reverse_dict = {}
for k, v in my_dict2.items():
    # v key in reverse dict : (value that already has, if any, or an empty list) + the older k key, which now is the value, added to the list
    reverse_dict[v] = reverse_dict.get(v, []) + [k]
# K is a list!! gives empty list if it's first value, then join K as list
print(reverse_dict)


print("")
