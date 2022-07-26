#LIST COMPREHENSION
# 
#version 1 --> [expression + FOR item + IN iterable + IF condition]
# version 2 --> [expression + IF/ELSE condition + FOR item + IN iterable]
print("List Comprehension")

squaresV1 = [i*i for i in range(1,30) if i%2==0]
print(squaresV1)

squaresV2 = [i*i if i%2==0 else i for i in range(1,30)]
print(squaresV2)

print("")


#REVERSE A LIST
#
# method1 --> slice
# method2 --> function
# method3 --> method
print("Reverse a List")
values = [1,2,3,4,5,6]

values1 = values[-1::-1]
print(values1)

values2 = list(reversed(values))
print(values2)

values.reverse()
print(values)

print("")


