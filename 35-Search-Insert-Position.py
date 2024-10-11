class Solution(object):
    def searchInsert(self, nums, target):
        if(target in nums):
            return nums.index(target)
        else:
            if(nums[0]>target):
                return 0
            elif(nums[len(nums)-1]<target):
                return len(nums)
            else:
                for i in range(len(nums)):
                    if(nums[i]<target and nums[i+1]>target):
                        return i+1 
    