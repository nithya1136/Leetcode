class Solution(object):
    def addBinary(self, a, b):
        s = list(a)
        t = list(b)
        r = []
        if len(a) < len(b):
            c = len(b) - len(a)
            for _ in range(c):
                s.insert(0, '0')
        elif len(a) > len(b):
            c = len(a) - len(b)
            for _ in range(c):
                t.insert(0, '0')
        carry = 0
        for i in range(len(s) - 1, -1, -1):
            sum_val = int(s[i]) + int(t[i]) + carry
            if sum_val == 0:
                r.insert(0, '0')
                carry = 0
            elif sum_val == 1:
                r.insert(0, '1')
                carry = 0
            elif sum_val == 2:
                r.insert(0, '0')
                carry = 1
            elif sum_val == 3:
                r.insert(0, '1')
                carry = 1
        if carry == 1:
            r.insert(0, '1')
        return ''.join(r)
