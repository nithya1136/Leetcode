class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        num = 0
        res = \\
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)  
            elif char == '[':
                st.append((res, num))  
                res, num = \\, 0 
            elif char == ']':
                prev, repeat = st.pop()  
                res = prev + res * repeat  
            else:
                res += char 
        return res