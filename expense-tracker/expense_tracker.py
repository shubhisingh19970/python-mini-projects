#create a list
my_list = [3]
#You can add an item to the end of a list using the append() method
my_list.append(1)
print(my_list)
#To access an element you use bracket notation. For example, example_list[1] is accessing the element at index 1, the second element, of example_list.
print(my_list[0])
my_list[0]=0
print(my_list)
#The insert method can add an element at any position in a list
my_list.insert(2,2)
print(my_list)
my_list.insert(3,3)
print(my_list)