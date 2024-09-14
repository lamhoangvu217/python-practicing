# Set Operations: Write a function that takes two sets and returns a tuple containing the union, intersection, 
# and difference of the sets.

def setsToTuple(set1, set2):
    unionSet = set1.union(set2)
    intersectionSet = set1.intersection(set2)
    differenceSet = set2.difference(set1)
    unionTuple = tuple(unionSet)
    intersectionTuple = tuple(intersectionSet)
    differenceTuple = tuple(differenceSet)
    
    print(unionTuple,intersectionTuple,  differenceTuple)
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7,8}
setsToTuple(set1, set2)