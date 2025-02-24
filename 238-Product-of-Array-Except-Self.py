class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        t = math.prod(nums)        
        for i in range(len(nums)):
            if nums[i] != 0:
                l.append(t // nums[i])  
            else:
                s = copy.deepcopy(nums)  
                s.pop(i)  
                l.append(math.prod(s))       
        return l