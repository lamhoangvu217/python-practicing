# Merge Dictionaries: Write a function that takes two dictionaries and merges them into one. 
# If there are duplicate keys, the value from the second dictionary should overwrite the value from the first dictionary.

def mergeDictionary(dictA, dictB):
    mergedDict = dictA.update(dictB)
    print(mergedDict, dictA)

dictA = { "a": "A Letter", "b": "B Letter", "c": "C Letter" }
dictB = { "d": "D Letter", "e": "E Letter", "f": "F Letter", "a": "AAA Letter" }
mergeDictionary(dictA, dictB)