class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a=set(nums1)
        b=set(nums2)
        l=[]
        s=[]
        for i in a:
            if(i not in b):
                l.append(i)
        for j in b:
            if(j not in a):
                s.append(j)
        return[l,s]
