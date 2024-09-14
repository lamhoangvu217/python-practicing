class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = self.get_index_binary(nums, target)
        if idx != -1:
            return self.get_same_index_value(nums,idx)
        else:
            return [-1,-1]

    def get_index_binary(self, nums, target):
        start_ = 0
        end_ = len(nums)
        if start_ - end_ == 1:
            return -1 if nums[0] != target else 0
        while end_ - start_ > 1:
            idx = (start_ + end_)//2
            if target == nums[idx]:
                return idx
            if target > nums[idx]:
                start_ = idx
            else:
                end_ = idx
        return -1
    
    def get_same_index_value(self,nums,idx):
        stack_up = 0
        stack_down = 0
        while True:
            check = False
            if nums[idx] == nums[idx+stack_up]:
                stack_up += 1
                check = True
            if nums[idx] == nums[idx+stack_down]:
                stack_down -=1
                check = True
            if check == False:
                break
            else:
                stack_check = 1
        return [idx+stack_down+stack_check, idx+stack_up-stack_check]

# print(Solution().searchRange([5,7,7,8,8,10],6))
print(Solution().searchRange([1],1))