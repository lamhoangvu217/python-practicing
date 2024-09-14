# Find the largest number which is smaller than x in the array
# input: array = [2,3,4,5,6,7,8,9], x = 5
# ouput: 4
def findXIndex(inputArr, target): 
    left = 0
    right = len(inputArr) - 1
    while left <= right:
        mid =  (left + right)// 2
        if inputArr[mid] == target:
            return mid
        elif inputArr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def findLargestNumberSmallerThanX():
    array = [2,3,4,5,6,7,8,9]
    x = 2
    smallestNum = 0
    targetIndex = findXIndex(array, x)

    if targetIndex > 0:
        return array[targetIndex - 1]
    elif targetIndex == 0:
        return array[targetIndex]
    else:
        return -1

print(findLargestNumberSmallerThanX())