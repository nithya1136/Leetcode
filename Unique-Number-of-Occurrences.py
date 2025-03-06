class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s=set(arr)
        l=[]
        for i in s:
            if arr.count(i) in l:
                return False
            else:
                l.append(arr.count(i))
        return True