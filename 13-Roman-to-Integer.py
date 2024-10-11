class Solution(object):
    def romanToInt(self, s):
        s=list(s)
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        r=0
        c=0
        for i in s:
            if(c!=0):
                if(dict[j]<dict[i]):
                    r=r-dict[j]+(dict[i]-dict[j])
                else:
                    r=r+dict[i]
                c+=1    
            else:
                r=r+dict[i]
                c+=1
            j=i
        return r                
        