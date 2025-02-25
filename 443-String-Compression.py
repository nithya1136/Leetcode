class Solution:
    def compress(self, chars: List[str]) -> int:
        s = []
        t = []  
        count = 1
        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[i - 1]:
                count += 1
            else:
                s.append(chars[i - 1])
                t.append(str(count) if count > 1 else '')
                count = 1       
        chars.clear()
        for i in range(len(s)):
            chars.append(s[i])
            if t[i]:
                chars.extend(list(t[i]))
        return len(chars)
