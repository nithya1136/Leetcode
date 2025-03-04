class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a','e','i','o','u']
        ma=0
        cu=0
        for i in range(k):
            if(s[i] in vowels):
                cu+=1
        ma=cu
        for i in range(k,len(s)):
            if(s[i] in vowels):
                cu+=1
            if(s[i-k] in vowels):
                cu-=1
            ma=max(ma,cu)
        return ma
