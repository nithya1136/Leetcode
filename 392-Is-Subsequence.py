class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = list(s)
        b = list(t)
        i = 0  
        for char in b:
            if i < len(a) and char == a[i]: 
                i += 1
        return i == len(a)