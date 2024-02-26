my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
my_list.insert(1, 15)
print(my_list)
my_list.extend([50, 60, 70])
print(my_list)
# remove last element
my_list.pop()
print(my_list)
# sort the list in ascending order
my_list.sort()
print(my_list)
# find and print the index of 30
print(my_list.index(30))
