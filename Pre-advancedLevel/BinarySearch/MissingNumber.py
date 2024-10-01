# https://leetcode.com/problems/missing-number/

def missingNumber(nums):
    sortedNums = sorted(nums)
    start = 0
    end = len(sortedNums)
    while start < end:
        mid = (start + end) // 2    
        if sortedNums[mid] > mid:
            end = mid
        else: 
            start = mid + 1
    return start 
nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))