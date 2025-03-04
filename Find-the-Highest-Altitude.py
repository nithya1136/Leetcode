class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a = 0
        max_a = 0
        for i in gain:
            a += i
            max_a = max(max_a, a)
        return max_a