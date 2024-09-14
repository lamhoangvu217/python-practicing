# Find the smallest number which is larger than x in the array  
# input: array = [2,3,4,5,6,7,8,9], x = 5
# ouput: 6
def findSmallestNumberLargerThanX(array, x):
    left = 0
    right = len(array) - 1
    result = -1  # Default to -1 if no valid number is found
    
    while left <= right: # 0
        mid = (left + right) // 2 # 3 (5) # 0 + 4 / 2 = 2
        if array[mid] > x: # 7 > 5
            result = array[mid]  # This could be the smallest larger number # 7
            right = mid - 1  # Try finding an even smaller larger number # 
        else:
            left = mid + 1  # Keep searching in the right half # 3 - 1 = 4
    
    return result

# Test the function
array = [2, 3, 4, 5, 6, 7, 8, 9]
x = 5
print(findSmallestNumberLargerThanX(array, x))