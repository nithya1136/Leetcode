class Solution(object):
    def containsDuplicate(self, nums):
        s=set(nums)
        if len(nums)!=len(s):
            return True
        else:
            return False
        