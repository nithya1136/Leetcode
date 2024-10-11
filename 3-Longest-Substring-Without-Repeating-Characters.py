class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        t = []
        max_length = 0  
        for i in s:
            if i in t:
                t = t[t.index(i) + 1:]
            t.append(i)
            max_length = max(max_length, len(t))
        return max_length      



