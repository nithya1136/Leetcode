class Solution(object):
    def isHappy(self, n):
        t = n
        sum = 0
        s = set()  
        while True:
            l = t % 10
            sum += l ** 2
            t = t // 10
            if t == 0:  
                if sum == 1:
                    return True
                elif sum in s:  
                    return False
                else:
                    s.add(sum)  
                    t = sum  
                    sum = 0  