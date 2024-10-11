class Solution(object):
    def getRow(self, rowIndex):
        o = []
        p = []
        for i in range(1, rowIndex + 2):  
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
        if 0 <= rowIndex < len(o):
            return o[rowIndex]
        else:
            raise IndexError(\rowIndex is out of range\)

