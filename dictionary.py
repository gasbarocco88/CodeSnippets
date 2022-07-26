#REVERSE A DICT
print("Reverse a Dict")
#unique value, with dict comprehension
my_dict = {"A":1, "B":2, "C":3, "D":4}
inv_dict = {v: k for k, v in my_dict.items()}
print(inv_dict)

#not unique value
my_dict2 = {"A":1, "B":2, "C":3, "D":1}
reverse_dict = {}
for k, v in my_dict2.items():
    reverse_dict[v] = reverse_dict.get(v, []) + [k] # K list!! gives empty list if it's first value and then adds K as list
print(reverse_dict)

print("")