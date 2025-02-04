class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        p = []
        j = 0 
        while True:
            try:
                char = strs[0][j]
                for word in strs:
                    if word[j] != char:
                        return "".join(p)
                p.append(char)
                j += 1
            except IndexError: 
                return "".join(p)
