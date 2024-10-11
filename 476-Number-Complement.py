class Solution(object):
    def findComplement(self, num):
        t=num
        s=[]
        c=0
        while(t):
            l=t%2
            s.append(l)
            t=t//2
            c+=1
        res=0
        for i in range(len(s)-1,-1,-1):
            if(s[i]==1):
                res=res*10+0
            else:
                res=res*10+1       
        return self.result(res)
    def result(self,a):
        n=0
        j=0
        while(a):
            i=a%10
            n=n+pow(2,j)*i
            j+=1
            a=a//10
        return n
