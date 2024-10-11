class Solution(object):
    def reverse(self, x):
        is_negative = x < 0
        x = abs(x)
        s = 0     
        while x:
            l = x % 10
            s = s * 10 + l
            x //= 10
        if s > 2147483647:  
            return 0
        return -s if is_negative else s
