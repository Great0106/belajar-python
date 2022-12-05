fruits = ("apple", "banana", "cherry", "melon", "kiwi")
#print(type(fruits))

fruit_list = list(fruits)
print(type(fruit_list))
print(fruit_list)

fruit_list[0] = "star fruit"
print(fruit_list)

fruits = tuple(fruit_list)
print(type(fruits))
print(fruits)
