class Solution(object):
    def removeElement(self, nums, val):
        c=0
        k=0
        for i in nums:
            if i==val:
                c+=1
            else:
                nums[k]=nums[nums.index(i)]
                k+=1
        return k
        