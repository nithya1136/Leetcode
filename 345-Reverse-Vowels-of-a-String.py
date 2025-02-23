class Solution:
    def reverseVowels(self, s: str) -> str:
        l=list(s)
        t=[]
        for i in range(len(l)):
            if(l[i]=='a' or l[i]=='e' or l[i]=='i' or l[i]=='o' or l[i]=='u' or l[i]=='A' or l[i]=='E' or l[i]=='I' or  l[i]=='O' or l[i]=='U'):
                t.append(i)
        j=len(t)-1
        i=0
        while(i<=j):
            l[t[i]],l[t[j]]=l[t[j]],l[t[i]]
            i+=1
            j-=1
        return ''.join(l)