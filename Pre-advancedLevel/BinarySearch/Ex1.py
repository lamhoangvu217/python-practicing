# Exercise 1: Find x in the array

# input: array = [2,3,4,5,6,7,8,9], target = 7
# output: index of 7 = 5

# base case: found item at mid, return item. can't find item, return -1
def findX(inputArr, target):
    left = 0
    right = len(inputArr) - 1
    while left <= right:
        mid = (left + right) // 2
        if inputArr[mid] == target:
            return mid
        elif inputArr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

array = [-1,0,3,5,9,12]
target = 2
print(findX(array, target))