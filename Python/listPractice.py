# LIST COMPREHENSION
# version 1 --> [expression + FOR item + IN iterable + IF condition]
squaresV1 = [i * i for i in range(1, 30) if i % 2 == 0]
print(squaresV1)

# version 2 --> [expression + IF/ELSE condition + FOR item + IN iterable]
squaresV2 = [i * i if i % 2 == 0 else i for i in range(1, 30)]
print(squaresV2)


print("")
# REVERSE A LIST
values = [1, 2, 3, 4, 5, 6]
# method1 --> slice
values1 = values[-1::-1]
print(values1)

# method2 --> function
values2 = list(reversed(values))
print(values2)

# method3 --> method
# it modifies the original list in place
values.reverse()
print(values)


print("")
