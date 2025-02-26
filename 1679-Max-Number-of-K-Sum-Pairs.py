class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        t = [num for num in nums if num < k]  
        t.sort() 
        i, j = 0, len(t) - 1  
        c = 0  
        while i < j:
            if t[i] + t[j] == k:  
                c += 1
                i += 1 
                j -= 1  
            elif t[i] + t[j] < k: 
                i += 1
            else:  
                j -= 1
        return c