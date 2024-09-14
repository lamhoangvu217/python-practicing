# Reverse a List: Write a function that takes a list and returns a new list with the elements in reverse order.

lists = [int(x) for x in input("Enter list with space: ").split()]
def reverseLists(list): 
    reversedList = list[::-1]
    return reversedList
print(reverseLists(lists))