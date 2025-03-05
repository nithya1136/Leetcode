class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=copy.deepcopy(nums)
        pivot=-1
        for i in range(len(nums)):
            if i==0:
                left=0
            else:
                left=sum(s[:i])
            right=sum(s[i+1:])
            if(left == right):
                pivot=i
                break
        return pivot
        