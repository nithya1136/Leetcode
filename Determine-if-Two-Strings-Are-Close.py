class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        a=Counter(word1)
        b=Counter(word2)
        if(sorted(a.values())==sorted(b.values())):
            return True
        return False
        