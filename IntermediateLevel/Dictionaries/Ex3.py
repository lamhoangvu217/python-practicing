# Find the Key with Maximum Value: Write a function that takes a dictionary where the values are numbers 
# and returns the key with the highest value.

def highestValueKey(dictA):
    maxValue = max(dictA, key=dictA.get)
    print(maxValue)
dictA = { "a": 7, "b": 8, "c": 5, "d": 2 }
highestValueKey(dictA)
