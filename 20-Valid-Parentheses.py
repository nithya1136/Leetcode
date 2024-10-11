class Solution(object):
    def isValid(self, s):
        l=[]
        for i in s:
            if (i=='(' or i=='{' or i==\[\):
                l.append(i)
            if(i==')'):
                if('(' not in l):
                    return False
                elif(l[len(l)-1]=='('):
                    l.pop()
            if(i=='}'):
                if('{' not in l):
                    return False
                elif(l[len(l)-1]=='{'):
                    l.pop()
            if(i==']'):
                if('[' not in l):
                    return False
                elif(l[len(l)-1]=='['):
                    l.pop()
        if len(l):
            return False
        else:
            return True

                            


