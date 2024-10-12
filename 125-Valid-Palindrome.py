class Solution(object):
    def isPalindrome(self, s):
        l=list(s)
        l1=[element.lower() for element in l if element.isalnum()]
        l2=l1[::-1]
        if(l2==l1):
            return True
        else:
            return False
        