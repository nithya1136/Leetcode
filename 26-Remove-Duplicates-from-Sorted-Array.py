class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        k = 0  
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1 
        return k 
