class Solution(object):
    def isPalindrome(self, x):
        if(x<0):
            return False
        else:
            t=x
            s=0
            while(t!=0):
                l=t%10
                s=s*10+l
                t=t//10
            if(s==x):
                return True
            else:
                return False    
        