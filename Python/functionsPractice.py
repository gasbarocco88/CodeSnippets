# LAMBDA
# --> lambda parameters : expressions (with if/else)
# useful if needed for a short period of time, but only one expression
sum = lambda x, y: x + y
print(sum(5, 3))

age_check = lambda age: "OK" if age >= 18 else "NO"
print(age_check(22))


print("")
# MAP
# apply a function to all item of an iterable
# gives a map object that has to be converted into a list
# not used anymore because of list comprehension
nums = [1, 2, 3, 4, 5, 6]
nums2 = list(map(lambda x: x * x, nums))
print(nums2)


print("")
# FILTER
# Filter a list of item using a certain criteria of function
# gives a filter object that has to be converted into a list
numslist = [1, 2, 3, 4, 5, 6]
numslist2 = list(filter(lambda x: x % 2 == 0, nums))
print(numslist2)


print("")
# ZIP FUNCTION
# combine items of different iterables
# gives a zip object that has to be converted into a list
animals_list = ["cat", "dog", "bird", "fish"]
animal_names = ["Billy", "Jack", "Tweety", "Nemo"]
animals_ages = [3, 5, 2, 7]
print(list(zip(animals_list, animal_names, animals_ages)))


print("")
# ENUMERATE FUNCTION
# create a tuple with (index:item) structure for every item in a list
# gives an enumerate object that has to be converted into a list
# used for taking item with its index in one same cycle
animals_list1 = ["cat", "dog", "bird", "fish"]
print(list(enumerate(animals_list1)))

for index, name in enumerate(animals_list1):
    print(f"{index+1}:{name}")


print("")
