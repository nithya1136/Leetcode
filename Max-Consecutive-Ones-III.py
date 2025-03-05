class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        l = 0
        z = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                z += 1
            while z > k:
                if nums[left] == 0:
                    z -= 1
                left += 1  
            l = max(l, right - left + 1)
        return l