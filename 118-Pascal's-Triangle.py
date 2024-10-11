class Solution(object):
    def generate(self, numRows):
        o = []
        p = []
        for i in range(1, numRows + 1):
            l = []
            for j in range(1, i + 1):
                if j == 1 or j == i:
                    t = 1
                    l.append(t)
                    if j == i:
                        p = []  
                else:
                    t = p[j - 2] + p[j - 1]  
                    l.append(t)
            p = l  
            o.append(l) 
        return o
        