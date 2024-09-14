# Sort a List of Tuples: Write a function that sorts a list of tuples based on the second element of each tuple. 
# For example, given [('a', 3), ('b', 1), ('c', 2)], 
# the function should return [('b', 1), ('c', 2), ('a', 3)].



def tupleSorting():
    # Creating a Tupl
    listsOfTuple = [('a', 3), ('b', 1), ('c', 2)]
    listsOfTuple.sort(key=lambda a: a[1])
    print(listsOfTuple)
tupleSorting()