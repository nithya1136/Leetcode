class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        s=[]
        l = [candies[i] + extraCandies for i in range(len(candies))]
        for i in range(len(l)):
            if(l[i]>=max(candies)):
                s.append(True)
            else:
                s.append(False)
        return s