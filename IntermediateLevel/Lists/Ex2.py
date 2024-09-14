# Remove Duplicates: Write a function that removes duplicates from a list while maintaining the original order of elements.
lists = [1,3,4,1,4,5,6,9] # expected result: [1,3,4,5,6,9]
# Method 1: sort
lists.sort()
result = []
for i in range(len(lists)): # get index of element in array
        if i == 0 or lists[i] != lists[i - 1]:
            result.append(lists[i])
print(result)